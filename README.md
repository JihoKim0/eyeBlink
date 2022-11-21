# eyeBlink
eye blink recognition with openCV &amp; dlib<br>


#Adam optimizer
https://ropiens.tistory.com/90<br>
장점 : 간단한 구현으로 효율적인 연산이 가능하고, 메모리 요구 사항이 거의 없다.<br>
gradient의 diagonal rescaling에 독립적이기때문에 파라미터마다 학습률을 다르게 조정할 수 있다.<br>
Adam의 hyper-parameter(Exponential Decay Rates)는 직관적이고, 조정이 거의 필요 없다.<br>
<br>
기존 Stochastic gradient-based optimization의 단점:<br>
object function에 잡음 발생 시 optimization 성능이 저하된다<br>
대표적인 nosie로 dropout regularization이 있음<br>
* dropout : 신경망의 일부 뉴런을 랜덤으로 OFF<br>
object function에 noise가 생긴다면, 더 효율적인 stochastic optimization이 요구됨<br>

