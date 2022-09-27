# Makefile

- Exists purely for automation
- Language and paradign agnostic
- Expects one or more input files to generate one or more output files

## Assigment operators

- **Verbatim assigment**:    `SRCS = main.c`
- **Simple expansion**:      `SRCS := $(wildcard *.c)`
- **Shell output**:          `SRCS != find . -name '*.c'`
                             `SRCS := $(shell find . -name '*.c')`
- **Conditional assigment**: `CFLAGS ?= $(CC_FLAGS)`
- **Append to**:             `CC_FLAGS += -Wextra`

## Built in functions

- $(SRCS:.c=.0)
- $(addprefix build/,$(OBJS))
- $(if ..) $(or ..) $(and ..)
- $(foreach var,list,text)
- $(value (VARIABLE))
- $(shell ..)
- $(error ..)
- $(warning ..)
- $(info ..)

## Rules

- Rules are shell commands emitted by make to produce an output file
- Rules use pattern matching on file types. The rule Make uses depends on how
  the recipe is configured
- There are many implicit rules built into Make for different file types
- Implicit rules become obselete very quickly

eg:
Target: dependencies
    actions

```makefile
%.o: %.c
    $(CC) -c $(CFLAGS) -o $@ $<
```

## Recipes

- First defined target is executed if none specified

```makefile
SRCS = main.c
OBJS := $(SRCS:.c=.o)
TARGETS := foo

.PHONY: all clean

all: $(TARGET)

foo: $(OBJS)
    $(CC) -o $@ $^

clean:
    rm -f $(OBJS)
```

## Automatic variables

- `$@` = Current target
- `$<` = First prerequisite
- `$^` = All prerequisite
- `$?` = Prerequisite that have changed
- `$|` = Order-only prerequisite

```makefile
SRCS = main.c
OBJS := $(SRCS:.c=.o)
DIR := build
OBJS := $(addprefix $(DIR), $(OBJS))
TARGET := foo

.PHONY: clean

$(DIR)/%.o: %.c
    $(CC) -c $(CFLAGS) -o $@ $<

$(TARGET): $(OBJS) | $(DIR)
    $(CC) -o $@ $^

$(DIR):
    mkdir -p $@
```

## Automatic dependency

- Make integrates with the compiler
- Dependency files contain information
    - MT: Name of the target
    - MMD: List user header files
    - MP: Add PHONY TARGETS
    - MF: Name of the file
- DEPFILES recipe and the include line must be the last line in the file
- Make will only rebuild prerequisites which have a newer timestamp than the
  generated dependency file

```makefile
DEPDIR = .dep
DEPFILES := $(SRCS:%.c=$(DEPDIR)/%.d)
DEPFLAGS = -MT $@ -MMD -MP -MF $(DEPDIR)$*.d

%.o: %.c $(DEPDIR)/%.d | $(DEPDIR)
    $(CC) -c $(CFLAGS) $(DEPDFLAGS) -o $@ $<

$(DEPDIR):
    @mkdir -p $(DEPDIR)

$(DEPFILES):

include $(wildcard $(DEPFILES))
```

## Template Makefile

```makefile
SRCS := $(wildcard *.c)
OBJDIR = .build
OBJS := $(SRCS:%.c=$(OBJDIR)/%.o)

DEPDIR = .dep
DEPS := $(SRCS:%.c=$(DEPDIR)/%.d)
DEPFLAGS = -MT $@ -MMD -MP -MF $(DEPDIR)/$*.d

.PHONY: clean
TARGET = foo

$(OBJDIR)/%.o: %.c | $(OBJDIR) $(DEPDIR)
    @echo [cc] $@
    @$(CC) -c $(CFLAGS) $(DEPFLAGS) -o $@ $<

$(TARGET): $(OBJS)
    @echo [LD] $@
    @$(CC) $(LDFLAGS) -o $@ $^

clean:
    @rm -rf $(OBJDIR) $(DEPDIR) $(TARGET)

$(OBJDIR) $(DEPDIR):
    @mkdir -p $@

$(DEPFILES):

include $(wildcard $(DEPFILES))
```

