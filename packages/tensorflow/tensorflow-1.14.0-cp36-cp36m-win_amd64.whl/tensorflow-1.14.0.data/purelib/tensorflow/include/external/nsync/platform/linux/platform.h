/* Copyright 2016 Google Inc.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. */

#ifndef NSYNC_PLATFORM_LINUX_PLATFORM_H_
#define NSYNC_PLATFORM_LINUX_PLATFORM_H_

#if !defined(_GNU_SOURCE)
#define _GNU_SOURCE /* for futexes */
#endif

#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>
#include <stddef.h>
#include <time.h>
#include <inttypes.h>
#include <limits.h>
#include <linux/futex.h>
#include <sys/syscall.h>
#include <pthread.h>
#include <semaphore.h>

#include <stdio.h>
#include <stdarg.h>

#endif /*NSYNC_PLATFORM_LINUX_PLATFORM_H_*/
