#include <errno.h>
#include <fcntl.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <sys/sysinfo.h>

#define EXIT_ERR_TOO_MANY_ARGS 1
#define EXIT_ERR_UNABLE_TO_OPEN_FILE 2
#define INTERVAL 2

#define MAX_LINE_LENGTH 1024

void log_performance(const char *log_file);
void sig_handler(int sigtype);

int main(int argc, char *argv[]) {
  if (argc != 2) {
    fprintf(stderr, "Usage: %s <file>\n", argv[0]);
    exit(EXIT_ERR_TOO_MANY_ARGS);
  }

  if (signal(SIGINT, sig_handler) == SIG_ERR) {
    perror("Error initializing signal handler");
    exit(errno);
  }

  log_performance(argv[1]);
}

void log_performance(const char *log_file) {
  unsigned long long user, system, idle;
  char line[MAX_LINE_LENGTH];
  const char proc_stat_file[] = "/proc/stat";
  long prev_total_cpu_time = 0, prev_idle_cpu_time = 0;
  double cpu_usage = 0.0;

  struct tm *timeinfo;
  time_t rawtime;
  char cur_time[20];

  struct sysinfo si;
  long total_memory, free_memory, used_memory;
  double memory_usage;

  FILE *fout = fopen(log_file, "w");
  if (!fout) {
    perror("Error opening output file");
    exit(EXIT_ERR_UNABLE_TO_OPEN_FILE);
  }

  while (1) {
    FILE *fin = fopen(proc_stat_file, "r");
    if (!fin) {
      perror("Error opening input file");
      fclose(fout);
      exit(EXIT_ERR_UNABLE_TO_OPEN_FILE);
    }
    while (fgets(line, sizeof(line), fin) != NULL && (strncmp(line, "cpu ", 4) != 0)) {
      // Do nothing, skip lines until the line starting with "cpu "
    }

    // skips 'cpu" token
    char *token = strtok(line, " ");
    int column = 1;
    long cpu_time = 0, total_cpu_time = 0, idle_cpu_time = 0;

    while ((token = strtok(NULL, " ")) != NULL) {
      cpu_time = strtol(token, NULL, 10);
      if (column++ == 4) idle_cpu_time = cpu_time;
      total_cpu_time += cpu_time;
    }

    cpu_usage = 100.0 * (total_cpu_time - prev_total_cpu_time - (idle_cpu_time - prev_idle_cpu_time)) / (total_cpu_time - prev_total_cpu_time);
    time(&rawtime);
    if ((timeinfo = localtime(&rawtime)) == NULL) {
      perror("Error getting local time");
      exit(errno);
    }

    if (sysinfo(&si) < 0) {
      perror("Error obtaining sysinfo");
      exit(errno);
    }
    total_memory = si.totalram / (1024 * 1024);
    free_memory = si.freeram / (1024 * 1024);
    used_memory = total_memory - free_memory;
    memory_usage = ((double) used_memory/ total_memory) * 100;

    strftime(cur_time, sizeof(cur_time), "%Y-%m-%dT%H:%M:%S", timeinfo);
    fprintf(fout, "[%s] - CPU: %.2f%%, MEM: %.2f%%\n", cur_time, cpu_usage, memory_usage);

    prev_total_cpu_time = total_cpu_time;
    prev_idle_cpu_time = idle_cpu_time;

    fclose(fin);
    sleep(INTERVAL);
  }

  fclose(fout);
}

void sig_handler(int sigtype) {
  printf("Closing performance logging");
  exit(EXIT_SUCCESS);
}
