# eyeBlink
eye blink recognition with openCV &amp; dlib<br>


#Adam optimizer<br>
https://keras.io/api/optimizers/adam/ <br>
Adam 클래스의 인수(arguments)로는 learning_rate, beta_1, beta_2, epsilon, amsgrad, name, **kwargs가 있다.<br>

https://ropiens.tistory.com/90<br>
초기에 필요한 4가지 파라미터는 다음과 같다.<br>
Stepsize α (Learing Rate)<br>
Decay Rates  β1, β2 : Exponential decay rates for the moment estimates (0~1 사이의 값) -> Adam의 유일한 hyper-parameter이며, gradient의 decay rate를 control 함<br>
Stochastic Objective Function f(θ)  // θ : parameters (weights) ->  f(θ) 값의 최소화가 adam의 목표<br>
initial Parameter Vector θ0<br>


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
