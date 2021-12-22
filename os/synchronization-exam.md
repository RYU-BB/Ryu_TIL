## Bounded-Buffer Problem

- 총 n개의 버퍼, 각각 한 개의 item을 가질 수 있다.
- mutex = 1, full = 0(현재 버퍼의 개수), empty = n(비어 있는 버퍼의 개수)
- 다양한 방식으로 풀 수 있다(이번엔 semaphore)
- producer - consumer

```
    // producer                    //consumer
    do {                             do {
    	// produce an item                
    	wait(empty);                      wait(full);
    	wait(mutex);                      wait(mutex);
    	// add an item to buffer          // remove an item from buffer
    	signal(mutex);                    signal(mutex);
    	signal(full);                     signal(empty);
    } while(true);                      // consume the item
       				     } while(true);
```

- mutex semaphore는 binary
- full, empty semaphore는 counting semaphore

기존 producer-consumer 문제점
- in, out방식은 버퍼를 한 개 사용못한다.
- count방식은 atomic을 보장하지 못한다.
- 3개의 semaphore로 해결

## Readers-Writers Problem
- rw_mutex = 1(semaphore), mutex = 1(semaphore), read_count = 0(int)
- rw_mutex : cs에 진입하기 위해서 cs에 실행중인 writer와 readers 또는 두 개 이상의 writers들의 경쟁이 이루어 진다.
- mutex : read_count값이 증가되거나 감소되는 것을 관리해줌 (atomic하게 보장해주기 위해)
- Readers - read만 한다.
  - 여러 개의 readers process가 동시에 여러 개에 접근하더라도 상관없다. 읽기만 하기 때문
- writers - read, write 둘다
  - writers는 다른 writers process와 같이 access할 수 없다.
  - 또한 다른 readers process와 같이 cs에 진입해선 안된다.
    
Problem1. writer가 기다리고 있는 경우, reader들은 다른 reader를 기다리지 않고 읽기 시작해야된다.
-> starvation: writer
Problem2. writer가 준비가 되어 쓰게되면, reader들이 읽기를 기다리고 있기 때문에 가능한 빨리 써야된다.
-> starvation: reader

```
// Writers
while (true) {
        wait(rw_mutex);
        /* writing is performed */
        signal(rw_mutex);
```
```
// Readers
while(true){
    wait(mutex);
    read_count++;
    if (read_count == 1) /* first reader */
            wait(rw_mutex);
            signal(mutex);
            
    /* reading is performed */
    
    wait(mutex);
    read count--;
    if (read_count == 0) /* last reader */
        signal(rw_mutex);
    signal(mutex);
```
readers가 더 우선순위인 코드다. why? 만약 writers와 readers가 경쟁해서 readers가 이긴 경우 뒤늦게 readers가 몇 개가 오든 동시에 cs에 접근이 가능하기 때문
반면에 writer는 경쟁에 이기더라도 다음 writer가 쓰이기 위해선 다시 경쟁을 해야된다.

따라서 writer starvation 가능성이 존재한다.

다른 방법으로 writer에 우선순위를 주는 방법이 있다. writer가 들어갈 의사표시를 하는 것만으로도 readers가 들어가지 못하도록 하는 방법도 있다.
하지만 readers에 starvation이 생기게 된다.

## Dining-Philosophers Problem
![img_1](https://user-images.githubusercontent.com/59256704/145119519-5c0ed1c1-e977-4615-ab33-08bd024a7d91.png)
- Philosophers(철학자)가 생각과 밥먹는 것을 계속 반복하는 것
- 철학자들은 옆의 사람들과는 절대 얘기를 나누지 않는다.
- 접시는 각자 쓰지만 각 젓가락은 옆사람과 공유하는 위치에 존재한다.
- 생각시(실행)엔 옆사람과 얘기할 필요가 없지만 밥먹기 위해선 양 옆의 철학자들과 공유하는 젓가락을 둘 다 집어야 가능하다

- Shared Data
  - Bowl of rice(data set)
  - Semaphore 젓가락[5] initialized to 1  
    
The structure of Philosopher i:
```
while (true) {
    wait(chopstick[i]);
    wait(chopstick[ (i + 1) % 5] ); //entry section
    
    /* eat for awhile */ (Critical section)
    
    signal (chopstick[i]); //exit section
    signal (chopstick[ (i + 1) % 5]);
    /* think for awhile */
    }
```
wait operation 두개를 통해 두 개의 젓가락을 확보한다.

- 모든 철학자가 wait(chipstick[i])을 실행하면 전부 젓가락을 하나씩 잡고 있는 상태이기 때문에 모두 두번째 wait을 실행할 수 없다.
이게 바로 deadlock 즉 잘못된 코드
- 5개의 semaphore가 상호 의존성을 지니면 deadlock이 생길 수 있다.
- deadlock handling
  - 4명만 앉아라
  - 동시에 2개를 잡을 수 있는 경우에만 젓가락을 잡아라 -> critical section
  - 홀수 먹은 후 짝수 먹고 이런 식
    
## Monitors
- Semaphore를 사용할 때에도 특정 실행 순서로 진행되었을 때만 발생하는 타이밍 오류는 여전히 발생한다.(순서가 일정하지 않기 때문에)
  - signal() -> wait()
    - 이 둘의 순서가 바뀌어 임계구역에 프로세스들이 동시에 진입하게 될 수 있다.
  - wait() -> wait()
    - deadlock이 발생한다.

![img_2](https://user-images.githubusercontent.com/59256704/145119543-687be1f8-361d-4298-9a40-8d233c8d9c56.png)

모니터 안에서 실행되는 프로세스는 단 한개만 가능 다른 프로세스들은 entry queue에서 대기

그래서 condition 변수를 추가하여 동시 접근과 동기화 문제를 해결한다.
- condition 변수
  - x.wait(): 실행중인 프로세스가 어떤 이벤트가 발생될 때까지 block되는 것
  - x.signal(): 정확히 하나의 일시중단된 프로세스를 재시작한다.
    
```
    monitor DiningPhilosophers {
    	enum {THINKING, HUNGRY, EATING} state[5]; # 헝그리는 생각, 먹기 사이의 단계 즉 젓가락 두개를 챙기는 단계
    	condition self[5]; # 컨디션 변수
    
    	void pickup(int i) { # 
    		state[i] = HUNGRY; // 배고프면 waiting에 넣기
    		test(i);
    		if(state[i] != EATING) self[i].wait(); #먹고 싶지만 젓가락이 둘 다 가용되지 않은 경우 셀프 wait
    	}
    	
    	void putdown(int i) {
    		state[i] = THINKING;
    		test((i + 4) % 5); // 다 먹은 state가 오른쪽인지 확인
    		test((i + 1) % 5); // 다 먹은 state가 왼쪽인지 확인
    	}
    	
    	void test(int i) { // 양쪽 state가 먹지 않는 상태이고 자신이 배고플 때 먹는다
    		if((state[(i + 4) % 5] != EATING && state[i] == HUNGRY && (state[(i + 1) % 5] != EATING)) {
    			state[i] = EATING;
    			self[i].signal();  # wait 중인 프로세스가 없을 경우 no effect
    	}
    
    	init() {
    		for(int i = 0; i < 5; ++i) {
    			state[i] = THINKING;
    		}
    }
```
No deadlock, but starvation is possible 젓가락 집는 걸 계속 기다릴 수 있다.

## Solaris synchronization
- adaptive mutexes 제공
  - 기본적으로 spin-lock으로 동작
  - 다른 cpu에서 실행중인 쓰레드에 의해서 lock이 동작
  - 현재 돌지않고 있는 쓰레드에 의해서 lock이 소비되고 있는 경우에는 낭비되기 때문에 block된다 lock이 realese됐다는 신호를 받을 때 까지
    
- condition 변수 그리고 reader-writers lock 사용
- adaptive mutex 또는 reader-writer lock을 사용할 때 lock의 우선순위를 어떻게 주는 가? 먼저들어가는 사람이 먼저 부여받음
- priority-inheritance protocol: lock이 릴리즈 돼야 높은 우선순위의 프로세스가 실행될 수 있으니 현재 실행중인 낮은 우선수위의 프로세스에게 잠시 높은 우선순위를 빌려주는 것

## Kernel Synchronization - Windows
- uniprocessor system에서는 주로 interrupt를 disable하는 방법을 많이 사용한다.
- multiprocessor에선 spinlocks을 사용

## Linux Synchronization
- 2.6버전 전에는 non-preemptive kernel 후에는 fully preemptive
- Linux provides:
  - atomic integers
  - spinlocks
  - semaphores
  - reader-writer versions of both (spinlock, semaphores)
    
atomic variables
- atomic_t is the type for atomic integer
- 리눅스가 제공하는 가장 간단한 형태의 툴
- atomic integers를 이용해 수학 연산을 하면 atomic operation이 보장된다.
- 즉 locking이 불필요

### mutex_lock, spin_lock
- 커널안에서 cs를 보여주기 위해 mutex_lock을 사용
- 빠져나올 때 mutex_unlock
- spin lock도 사용가능하며 semaphore도 사용 가능하다.
- single process에서는 kernel preemption을 enabling 하거나 disabling해서 locking 기능을 한다.

## Pthread(Posix) Synchronization
- 유저 레벨 쓰레드에서의 동기화 툴
- 유닉스나 리눅스 mac os에서 사용
- mutex locks, semaphore, condition variable 제공
- read-write locks, spinlocks 미제공

### POSIX Mutex Locks
- Fundamental synchronization tool used with Pthreads
- creating and initializing the lock
```
#include <pthread.h>

pthread mutex_t mutex;

pthread_mutex_init(&mutex, NULL);
```
- Acquiring and releasing the lock
``` 
pthread_mutex_lock(&mutex);

/* critical section */

pthread_mutex_unlock(*mutex);
```

### POSIX Semaphores
- named 그리고 unnamed 두 버전을 제공
- named는 서로 관련있는 프로세스가 아니어도 사용가능, unnamed는 서로 관련있는 프로세스끼리만 사용가능


### POSIX Named Semaphores
```
#include <semaphore.h>

sem_t *sem;

sem = sem_open("SEM", O_CREAT, 0666, 1);
```
```
sem_wait(sem); # acquire

sem_post(sem); # release
```

### POSIX Unnamed Semaphores
```
#include <semaphore.h>

sem_t *sem;

sem_init(&sem, 0, 1);
```
```
sem_wait(sem); # acquire

sem_post(sem); # release
```

### POSIX Condition Variables
monitor를 제공하지 않기 떄문에 monitor와 같은 역할을 하기 위해 condition변수를 제공
```
pthread_mutex_t mutex;
pthread_cond_t cond_var;

pthread_mutex_init(&mutex, NULL);
pthread_cond_init(&cond_var, NULL);
```

## Java Synchronization
- Java monitors
- Reentrant locks
- Semaphores
- Condition variables

### Java Monitors
- 모든 자바 오브젝트는 single lock을 갖고 있다. (오브젝트 내부의 각 메서드들이 동시에 실행될 수 없다.)
- 따라서 모든 메서드를 synchronized 해줄 필요가 있다.
```
public synchronized void insert(E item){
}
public synchronized E remove() {
}
```
signal에 해당되는 것이 notify() wait은 wait()

### Java Reentrant Locks
- mutex locks과 유사하다.
```
Lock key = new ReentrantLock();

key.lock();
try {
    cs
}
finally{
    key.unlock();
}
```

### Java Semaphores
- Constructor:
        `Semaphore(int value);`
- Usage:
        ```
        Semaphore sem = new Semaphore(1);
  
        try {
            sem.acquire();
            /* cs */
        }
        catch (InterruptedException ie) {}
        finally {
            sem.release();
        }

## Alternative Approaches
- Transactional Memory
- OpenMP
- Functional Programming Languages

### Transactional Memory


