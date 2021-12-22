## Chapter8: Deaklocks
- Deadlock Prevention
- Deadlock Avoidance
- Deadlock Detection

![img_3](https://user-images.githubusercontent.com/59256704/145119593-e1f6ac32-7561-47d1-b985-cbb675f43902.png)

- 2차선이었던 도로가 중간에 1차선이되는 지점에 양방향에서 동시에 차가 들어와서 오도가도 못하는 상황이 바로 deadlock
- 다리는 resource
- 한쪽 차가 피해줘야 된다. 이 것을 preemption이라고 볼 수 있다. 또는 rollback
- deadlock이 한 번 형성되면 여러 대의 차가 밀린다.

### deadlock with semaphores
- 둘다 wait상태라 아무 일도 일어날 수 없는 상태일 때 deadlock이라고 한다.

### livelock
- 데드락과 유사하지만 조금 다르다
- 데드락은 본인이 아닌 다른 쓰레드에 의해서만 가능하다.
- 라이브락은 블락이 된 것은 아니지만 의미 없는 행동만 반복하고 있는 것
- random time을 줘서 해결하는 방법이 있다.

### 프로세스가 자원을 사용하는 과정
1. request : 먼저 자원 요청을 한다. 자원을 즉시 얻을 수 없다면 얻을 수 있을 때까지 대기한다.
2. use: 자원을 얻은 프로세스는 할 일을 한다.
3. release: 할 일을 다 한 프로세스는 소유한 자원을 풀어놓는다.

## Deadlock의 네가지 발생조건
- Mutual exclusion: 오직 하나의 프로세스만 하나의 자원을 사용할 수 있다. 적어도 하나의 자원은 공유가 불가능한 자원이다.
- hold and wait: 적어도 하나의 자원을 보유한 프로세스가 다른 프로세스의 자원을 추가로 얻기를 기다릴 때
- no preemption: preemption이 불가능해야된다. 모든 리소스가 preemption가능하다면 데드락은 발생하지 않는다. 즉 이미 할당된 자원이 갑자기 반납되어서는 안된다.
- circular wait: 프로세스들이 자원을 소유하고 요청하는 형태가 원형을 이룰 때를 말한다. 즉 p1은 p2의 자원을 기다리고, p2는 p3의 자원을 기다리고, p3는 p1의 자원을 기다리고 ...

### Resource-allocation graph
시스템의 자원 할당 상황을 그래프로 그린 것 데드락을 판별하기 위해 만들어졌다.
![img_4](https://user-images.githubusercontent.com/59256704/145119604-e74b8940-1054-413c-ae9e-bd20bcf10fd9.png)

P는 프로세스, R은 시스템 내 자원 유형, R내부의 검은 점은 인스턴스를 나타낸다.

P->R로 향하는 화살표는 Request Edge: 프로세스가 해당 자원을 요청
R->P로 향하는 화살표는 Assignment Edge: 해당 자원이 프로세스에 할당되어 있음

Resource-allocation graph에 Cycle이 있으면, 데드락이 존재할 가능성이 있다.

가능성이므로 무조건 데드락이 존재하는 게 아니다.

그렇다면 어떤 것이 데드락이 발생한 조건일까?

가장 쉬운 상황은 모든 리소스 타입에 인스턴스가 하나밖에 없는데 사이클이 존재하는 경우다.

하지만 좀 더 정확히 데드락 상태를 확인하기 위해

Request Edge와 Assignment Edge의 상태를 분석해야 한다.


위 자료는 데드락상태이다. R2의 인스턴스가 두 개이지만 각각 P1과 P2에 할당되고 남은 자원이 없는 상태에서 P3가 request edge를 해 cycle이 생성됐기 때문이다.

![img_5](https://user-images.githubusercontent.com/59256704/145119620-a9aac9ad-3742-4e44-9f26-138363b6c3b7.png)
이 그래프도 cycle이 존재한다. 하지만 P4가 반납하면 P3가 써버리면 되기 때문에 데드락 상태가 풀려버린다.

따라서 데드락은 그래프에서 Cycle + Edge상태로 발생 여부를 판단해야 된다.


## Methods for Handling Deadlocks
데드락을 해결하는 방법에는 크게 네 가지가 있다.
1. 데드락 발생을 아예 prevent해서 발생 가능성이 0이 되게 한다.
2. 데드락 발생을 avoid하기 위해서 데드락 발생 가능성 여부가 있는지 계속 체크한다. 가능성이 조금이라도 있으면 어떤 조치를 취한다.
3. 데드락 상태를 detect하고 recover한다.
4. 데드락 상태를 그냥 ignore한다.

- 여기서 prevention은 process가 resource를 요구하는 방식에 제한을 두는 것이고,
- avoidance는 process의 resource 요청은 받아들이지만 만약 그 요청이 데드락이 발생할 가능성을 야기한다면, 그 요구를 거절하는 것이다.


### Deadlock Prevention
보통 데드락의 발생 조건을 기준으로 해결 방법을 찾는다. prevention은 시스템 성능을 떨어뜨리는 단점이 있다.

1) Mutual Exclusion: 프린터 같은 어떤 자원은 공유 자체가 불가능하고, 이런 자원들 때문에 Mutual Exclusion은 무조건 보장이 되어야 된다.
따라서 이 조건을 막아 Deadlock을 해결하겠다는 것은 불가능하다.
   
2) Hold and Wait: process가 어떤 자원을 요구할 때 모든 자원을 요청하고 할당받으려고 한다면 Hold and Wait 조건을 해결할 수 있어서 데드락 예방이 가능하다.
   - 프로세스가 필요로 하는 자원을 한 번에 다 요구를 해야 하니 한 번에 한 프로세스만 자원을 소유할 수 있겠죠?
   - 이런 것을 바로 All or Nothing 이라고 한다.
   - 자원의 낭비가 심해 효율성이 매우 떨어지게 되며 starvation이 발생하기 때문에 역시 이 방법도 불가능하다.
    
3) No preemption: 현실적으로 preemption을 허락해 주는 것이 Deadlock을 prevention하는데 효과적인 방법이다.
   - 사실 preemption을 허락해주지 않았기 때문에 데드락이 발생했던 것인데, 우선순위 높은 애가 자원을 뺏게 되면 데드락 떄문에 활용이 안 되던 점유된 자원을 뻇어 사용
   - 다만, (1) 자원이 뺏긴 프로세스는 현재까지의 작업이 무효화된다. (2)자원이 뺏겨 대기하던 프로세스가 다시 작업을 하려면 기존에 갖고 있던 old resource + 새로운 요구치 new resource를 다 할당 받아야 하는데 이 과정에서 starvation이 생길 수 있다는 단점이 있다.
    
4) Circular Wait: 만약 우리가 모든 리소스에 번호를 부여해서 프로세스들이 오름차순으로 자원을 요구한다면 우선순위 개념 때문에 Deadlock은 발생하지 않게된다.
   - 그러나 복잡해서 사용안한다. 프로세스 번호가 큰 자원을 할당받은 상태에서 낮은 자원이 요구한다면 자신의 자원을 내려놓고 낮은 자원을 할당 받은 뒤 다시 자기가 갖고 있던 우선순위 낮은 자원을 할당받아야 된다.
    
### Deadlock avoidance
데드락의 발생 가능성을 계속 검사해서 데드락 발생 가능성이 있다면 회피해 버리는 방식

데드락 회피를 위해 사용되는 개념은 Safe State와 Unsafe state이다.


![img_6](https://user-images.githubusercontent.com/59256704/145119637-19e395f7-97e4-4276-8c6d-428125f92c45.png)

데드락을 회피하기 위해선 Safe state에 있던 프로세스가 Unsafe state로 간다면 state를 바꾸게 한 행동을 찾아 행동을 취소하게 한다든지의 방식으로 다시 safe state로 돌아가게 만들어야 된다.

그렇다면 우린 이제 state가 어떤 상황인지를 파악할 일만 남았다. 그건 safe sequence를 통해 그 상황을 알 수 있다.

<br>

### Safe sequence
프로세스들이 현재 할당받은 자원과, 더 할당받고 싶어 하는 자원이 어떻게 되는지 파악하여, 어떤 순서로 자원을 할당했을 시 데드락은 발생하지 않고 모든 프로세스의 요구를 처리해줄 수 있는 순서를 말한다.

그리고 safe sequence가 하나라도 존재한다면, 그 state는 safe state이다.

![img_7](https://user-images.githubusercontent.com/59256704/145119655-a9be0797-fd3d-4496-8901-08414dc40b7c.png)

### resource allocation graph
이전에 다룬 resource allocation graph를 사용해 avoidance하는 방법도 있다.
![img_8](https://user-images.githubusercontent.com/59256704/145119674-ef2e9006-15e4-49a7-8c18-9d1ffa8f3668.png)

여기에 Claim edge를 추가한다.

Claim edge는 프로세스가 새로 요구하는 자원을 의미한다. 그리고 실제로 자원을 할당받으면 assignment edge로 바뀌게 된다.

위 그림은 claim edge를 제외하고 본다면 safe state지만 claim edge를 쏘고 있던 두 프로세스 중 누군가가 실제로 R2를 할당받아 assignment edge로 바뀐다면 그때부터는 cycle이 형성돼 unsafe state가 됩니다.
![img_9](https://user-images.githubusercontent.com/59256704/145119689-805c90de-a2b3-40db-8a55-a4770ce0ee82.png)
## Banker's Algorithm
resource allocation graph는 자원의 인스턴스가 하나인 경우였다.

이번엔 multiple instance of a resource의 경우엔 어떻게 해야되는지 알아보자.

Banker's Algorithm에서 사용하는 자료구조는
- available : 각 자원 별로 현재 남아있는, 이용 가능한 자원을 의미한다.
- Max : 각 프로세스의 자원별로 최대 요구하는 자원의 수를 의미한다.
- Allocation : 현재 각 프로세스에 할당되어 있는 자원별 자원의 수를 의미한다.
- Need : 각 프로세스의 자원 별 실행 종료를 위해 필요로 하는 남은 자원의 수를 의미한다.

Banker's algorithm에서 사용하는 두 가지 주요한 알고리즘
1) Safety Algorithm:
   (1) work와 finish를 각가 길이가 m과 n인 벡터로 가정. (m = 자원 타입의 수, n = 프로세스의 수)
       work = available
       finish[i] = False (for i = 1, 2, ..., n)
   (2) 아래의 상황에서 i를 계속 찾음
       a. Finish[i] == false
       b. Need(i) <= Work
       만약 이런 i값이 없으면 (4)로 이동
   (3) Work = Work + Allocation(i)
       Finish[i] = true
       Go to Step(2)
   (4) if Finish[i] == true for all i, 그렇다면 이 시스템은 safety state다
   

2) Resource Request Algorithm
Request(i)[j] = k라면, Pi는 Rj의 자원을 k개 요구한다는 것을 의미한다.
   
## Deadlock Detection
데드락 탐지는 Deadlock Recover와 한 세트라고 생각해도 된다.

기본적으로 1) 알고리즘을 통해 현재 시스템에 데드락이 있는지 찾고, 2) 알고리즘을 통해 데드락을 복구하는 것이다.

먼저 Resource allocation graph가 single instance of each resource type인 경우

Wait for Graph로 바꾼다.

single instance이기 때문에 cycle이 형성되어 있으면 바로 데드락이다.
![img_10](https://user-images.githubusercontent.com/59256704/145119705-1c7af1a6-a65e-43ed-9b17-5c4c9b533cf5.png)


만약 인스턴스에 자원이 여러 개 존재한다면 Deadlock detection algorithm을 사용해야 된다.

1) Work = Available, Allocation(i) != 0이면 Finish[i] = False (for i = 1, 2, ..., n)
2) Finish[i] == false, Request(i) <= Work 만약 이런 i값이 없으면 (4)로 이동
3) Work = Work+Allocation(i), Finish[i] = true, go to step(2)
4) Finish[i] = False 면, 0<= i < n인 범위에서 시스템은 데드락 상태에 있다.

## Deadlock Recovery
- 데드락을 회복하는 방법은 1) Abort one or more processes, 2) Preempt some resources 두 가지가 있다.

1) 먼저 프로세스를 죽이는 경우는 다시 두 가지로 나뉜다.
   1. Abort all deadlocked Processes
   2. Abort one process at a time -> 그 후 데드락이 풀리는지 check
    
   프로세스를 죽이는 방식이기 때문에 프로세스가 실행 중이던 결과가 값어치 있는 것이면 큰일난다.

따라서 어느 프로세스를 중지시킬 것인지 선택하는 요인들이 있다.

1) 프로세스의 우선순위, 2) 프로세스가 수행한 시간과 일을 끝마치는데 남은 시간, 3) 프로세스가 사용한 자원 타입과 양, 4) 프로세스가 종료하기까지 남은 자원의 수, 5) 얼마나 많은 수의 프로세스가 끝장나야 하는지 6) 프로세스가 interactive 인지 batch형태인지.

2) resource preemption은 프로세스를 죽이지 않고 자원만 뺐는다.
   1. Selecting a victim: 어느 프로세스의 어떤 자원을 뺏을지 결정해야 한다. 희생 비용을 최소화하기 위한 방법을 결정해야 한다.
   2. Rollback: 어떤 프로세스로부터 자원을 가져오면(선점하면) 그 프로세스를 어떻게 처리해야 하는 걸까요?
      자원이 뺏긴 프로세스를 safe state로 roll back하고 나중에 restart해야 한다. 아니면 그냥 처음의 상태로 돌려버리는 것도 가능
   3. starvation: 우선순위의 기준에 따라 희생하는 놈이 계속 희생을 하기 때문에 starvation이 발생할 수 있다. 따라서 희생 비용인 Cost factors에 Rollback 횟수를 포함시켜 희생자를 선택하게 만들어야 한다.
    
