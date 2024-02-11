#include <errno.h>
#include <fcntl.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <sys/sysinfo.h>

#define EXIT_ERR_INCORRECT_ARGS 1
#define EXIT_ERR_UNABLE_TO_OPEN_FILE 2
#define EXIT_ERR_UNABLE_TO_PARSE 3

#define INTERVAL 5
#define CPU_THRESHOLD 90.0
#define MEM_THRESHOLD 90.0

#define MAX_LINE_LENGTH 1024
#define MAX_LOG_LINE_LENGTH 100

void log_performance(const char *log_file);
void stat_performance(const char *log_file);
void sig_handler(int sigtype);
void bail(const char *statement);

int main(int argc, char *argv[]) {
  if (argc != 3 || (!(strcmp(argv[1], "stat") == 0 || strcmp(argv[1], "log") == 0))) {
    fprintf(stderr, "Usage: %s [stat|log] <file>\n", argv[0]);
    exit(EXIT_ERR_INCORRECT_ARGS);
  }

  if (signal(SIGINT, sig_handler) == SIG_ERR) {
    perror("Error initializing signal handler");
    exit(errno);
  }

  (strcmp(argv[1], "log") == 0) ? log_performance(argv[2]) : stat_performance(argv[2]);
}

void log_performance(const char *log_file) {
  // unsigned long long user, system, idle;
  char line[MAX_LINE_LENGTH];
  const char proc_stat_file[] = "/proc/stat";
  unsigned long long prev_total_cpu_time = 0, prev_idle_cpu_time = 0;
  double cpu_usage = 0.0;

  struct tm *timeinfo;
  time_t rawtime;
  char cur_time[20];

  struct sysinfo si;
  long total_memory, free_memory, used_memory;
  double memory_usage;

  char label[] = "INFO";

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
    unsigned int column = 1;
    unsigned long long cpu_time = 0, total_cpu_time = 0, idle_cpu_time = 0;

    // user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice
    while ((token = strtok(NULL, " ")) != NULL) {
      cpu_time = strtol(token, NULL, 10);
      if (column == 4) idle_cpu_time = cpu_time;
      if (column == 5) idle_cpu_time += cpu_time;
      total_cpu_time += cpu_time;
      column++;
    }

    cpu_usage = 100.0 * (total_cpu_time - prev_total_cpu_time - (idle_cpu_time - prev_idle_cpu_time)) / (total_cpu_time - prev_total_cpu_time);
    time(&rawtime);
    if ((timeinfo = localtime(&rawtime)) == NULL) {
      perror("Error getting local time");
      fclose(fin);
      fclose(fout);
      exit(errno);
    }

    if (sysinfo(&si) < 0) {
      perror("Error obtaining sysinfo");
      fclose(fin);
      fclose(fout);
      exit(errno);
    }
    total_memory = si.totalram / (1024 * 1024);
    free_memory = si.freeram / (1024 * 1024);
    used_memory = total_memory - free_memory;
    memory_usage = ((double) used_memory / total_memory) * 100;

    strftime(cur_time, sizeof(cur_time), "%Y-%m-%dT%H:%M:%S", timeinfo);
    (cpu_usage > CPU_THRESHOLD || memory_usage > MEM_THRESHOLD) ? strncpy(label, "WARN", 5) : strncpy(label, "INFO", 5);
    fprintf(fout, "[%s] %s - CPU: %.2f%%, MEM: %.2f%%\n", cur_time, label, cpu_usage, memory_usage);

    prev_total_cpu_time = total_cpu_time;
    prev_idle_cpu_time = idle_cpu_time;

    fclose(fin);
    fflush(fout);
    sleep(INTERVAL);
  }

  fclose(fout);
}

void stat_performance(const char *log_file) {
  FILE *fin = NULL;
  float cpu_max = 0.0, mem_max = 0.0;
  unsigned long line_count = 1;
  float cpu = 0.0, mem = 0.0;
  char line[MAX_LOG_LINE_LENGTH];
  // [2024-02-07T12:03:49] INFO - CPU: 100.00%, MEM: 100.00%
  
  if ((fin = fopen(log_file, "r")) == NULL) {
    fprintf(stderr, "Error opening file %s\n", log_file);
    exit(EXIT_ERR_UNABLE_TO_OPEN_FILE);
  }

  while (fgets(line, sizeof(line), fin)) {
    if (sscanf(line, "[%*[^]]] %*s - CPU: %f%%, MEM: %f%%", &cpu, &mem) != 2) {
      fprintf(stderr, "Error while parsing file %s at line %lu: %s\n", log_file, line_count, line);
      fclose(fin);
      exit(EXIT_ERR_UNABLE_TO_PARSE);
    };
    if (cpu > cpu_max) cpu_max = cpu;
    if (mem > mem_max) mem_max = mem;
    line_count++;
  }

  printf("MAX CPU: %.2f%%\n", cpu_max);
  printf("MAX MEM: %.2f%%\n", mem_max);
  fclose(fin);
}

void sig_handler(int sigtype) {
  printf("Closing performance logging\n");
  exit(EXIT_SUCCESS);
}

