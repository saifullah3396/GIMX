ifneq ($(DEBUG),1)
CFLAGS += -Wall -Wextra -Werror -O3 -fPIC
CXXFLAGS += -Wall -Wextra -Werror -O3 -fPIC
else
ifneq ($(OS),Windows_NT)
CFLAGS += -Wall -Wextra -Werror -O0 -g -fsanitize=address -fno-omit-frame-pointer -fPIC
CXXFLAGS += -Wall -Wextra -Werror -O0 -g -fsanitize=address -fno-omit-frame-pointer -fPIC
LDFLAGS += -fsanitize=address
else
CFLAGS += -Wall -Wextra -Werror -O0 -g -fno-omit-frame-pointer -fPIC
CXXFLAGS += -Wall -Wextra -Werror -O0 -g -fno-omit-frame-pointer -fPIC
endif
endif

CPPFLAGS = -I../..

LDFLAGS = -L../../gimxhid -L../../gimxpoll -L../../gimxlog -L../../gimxtime -L../../gimxtimer -L../../gimxprio
LDLIBS = -lgimxhid -lgimxpoll -lgimxlog -lgimxtime -lgimxtimer -lgimxprio

BINS=ghid_test
ifneq ($(OS),Windows_NT)
OUT=$(BINS)
else
OUT=ghid_test.exe
endif

all: $(BINS)

clean:
	$(RM) $(OUT) *~
