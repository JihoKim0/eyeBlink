# eyeBlink
eye blink recognition with openCV &amp; dlib<br>
<br><br>
딥러닝 모델 정확도 그래프<br>
https://mangastorytelling.tistory.com/entry/%EB%B9%B5%ED%98%95%EC%9D%98-%EA%B0%9C%EB%B0%9C%EB%8F%84%EC%83%81%EA%B5%AD-%EB%94%A5%EB%9F%AC%EB%8B%9D%EC%9C%BC%EB%A1%9C-%EB%88%88-%EA%B9%9C%EB%B9%A1%EC%9E%84-%EA%B0%90%EC%A7%80%EA%B8%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0-Python-Deep-Learning<br>
7:30~<br>
https://github.com/kairess/eye_blink_detector/blob/master/train.ipynb<br><br>
학습한 모델의 정확도를 확인해 보자. 모델의 accuracy를 출력하고 heatmap을 사용하여 그래프를 나타낸다.
confusion matrix-in[8]<br>
위의 결과와 같이 놀라운 정확도를 가진 모델을 생성한 것을 확인할 수 있다.



인식 결과를 히스토그램으로 나타내보면 다음과 같다.<br>
사진~(Distribution of Prediction-in[9])<br>
위의 결과와 같이 0 또는 1, 즉 감은 눈과 뜬 눈으로만 인식한 것을 확인할 수 있다.<br><br>

#Adam optimizer<br>
https://keras.io/api/optimizers/adam/ <br>
Adam 클래스의 인수(arguments)로는 learning_rate, beta_1, beta_2, epsilon, amsgrad, name, **kwargs가 있다.<br>

https://ropiens.tistory.com/90<br>
초기에 필요한 4가지 파라미터는 다음과 같다.<br>
Stepsize α (Learing Rate)<br>
Decay Rates  β1, β2 : Exponential decay rates for the moment estimates (0~1 사이의 값) -> Adam의 유일한 hyper-parameter이며, gradient의 decay rate를 control 함<br>
Stochastic Objective Function f(θ)  // θ : parameters (weights) ->  f(θ) 값의 최소화가 adam의 목표<br>
initial Parameter Vector θ0<br>

Adam의 알고리즘은 다음과 같다.<br>
1. 1st moment vector, 2nd moment vector, timestep을 초기화한다.
2. 파라미터 θ_t가 더 이상 수렴하지 않을 때 까지<br>
2-1. tiemstep 1 증가<br>
2-2. 이전 timestep의 gradient 계산을 통해 미분 수행<br>
2-3. biased first moment & second moment 계산<br>
2-4. bias-correction을 적용하여 초기의 모멘텀 값이 0으로 초기화되는 경우를 방지<br>
2-5. 가중치 갱신<br>

장점 : 간단한 구현으로 효율적인 연산이 가능하고, 메모리 요구 사항이 거의 없다.<br>
gradient의 diagonal rescaling에 독립적이기때문에 파라미터마다 학습률을 다르게 조정할 수 있다.<br>
Adam의 hyper-parameter(Exponential Decay Rates)는 직관적이고, 조정이 거의 필요 없다.<br>
<br>
기존 Stochastic gradient-based optimization의 단점:<br>
object function에 잡음 발생 시 optimization 성능이 저하된다<br>
대표적인 nosie로 dropout regularization이 있음<br>
* dropout : 신경망의 일부 뉴런을 랜덤으로 OFF<br>
object function에 noise가 생긴다면, 더 효율적인 stochastic optimization이 요구됨<br>

<br><br><br>
DB(sqlite limit)<br>
https://www.sqlitetutorial.net/sqlite-limit/ <br>
최근 일부 데이터만 가져오기 위해 sqlite의 limit절을 사용하였다.<br>
limit절은 결과집합을 불러올 때 레코드의 개수를 제한하여 가져올 때 사용한다.<br>
limit절은 다음과 같은 형태로 사용한다.<br>
SELECT column_list FROM table LIMIT row_count;<br>
추가적으로 해당 형태에 OFFSET 절을 추가하여 LIMIT의 시작 위치를 설정할 수 있다. 형태는 다음과 같다.
SELECT column_list FROM table LIMIT row_count OFFSET offset;<br>
혹은 다음과 같이 더 짧은 구문을 사용할 수도 있다.<br>
SELECT column_list FROM table LIMIT offset, row_count;<br>
본 논문에서는 데이터베이스의 크기가 가변하는 형태로, OFFSET절을 사용하지 않고, 내림차순 정렬 후 LIMIT절을 사용하여 최근 7개의 데이터를 가져오도록 하였다.<br>

