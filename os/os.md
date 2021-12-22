## Semaphore Implementation with no Busy waiting

- block: block함수를 호출한 프로세스를 waiting queue에 place해준다.
- wakeup: waiting queue에 있는 프로세스를 하나 꺼내서 ready queue에 삽입

## Monitor
- 고수준의 동기화 그러나 세마포어보다 훨씬 쉽다
- abstract data type(class와 비슷)

```
monitor monitor-name
{
    //shared variable declarations
    procedure P1 (...) {...}
    procedure Pn (...) {...}

        initialization code (...) {...}
}
}
```
![img](https://user-images.githubusercontent.com/59256704/145119745-7c71f3bc-b6bc-40d2-b6f6-e4b23b9f9153.png)
- Only one process at a time can be executing within monitor(모니터 내부에서 실행되는 프로세스는 한개로 제한한다.)
- 세마포어에 비해 강력한 도구는 아니다.

공유자원 + 공유자원에 접근하는 함수 + 2개의 Queue로 구성되어 있다.

mutual exclusion queue, conditional synchronization queue 두 개이다.

- mutual exclusion queue는 말 그대로 공유 자원에 하나의 프로세스만 진입하도록 하기 위한 큐이다.
- conditional synchronization queue는 이미 공유자원을 사용하고 있는 프로세스가 특정한 호출 wait()을 통해 조건동기 큐로 들어갈 수 있다.

conditional synchronization queue에 들어가 있는 프로세스는 공유자원을 사용하고 있는 다른 프로세스에 의해 깨워줄 수 있다. 이 역시 깨워주는 프로세스에서 특정한 호출 notify()을 해주며,
깨워주더라도 이미 공유자원을 사용하고 있는 프로세스가 해당 구역을 나가야 비로소 큐에 있던 프로세스가 실행된다.

