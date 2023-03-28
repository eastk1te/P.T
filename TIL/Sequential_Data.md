> 1. Neural Network Basics

one to one - 이진 분류
one to many - 이미지 캡션(이미지를 텍스트로)
many to one - 텍스트 입력에서 이미지
many to many - 기계 번역 등의 중요한 문제.

머신러닝은 파라미터를 직접 지정해줘야하는데, 신경망은 매우 유연하여 피처를 뽑아내는데 지도해주는 사람이 추가로 필요하지 않고 신경망에 의해 자동적으로 추출 됨.

신경망에서 마지막 step(activation) function은 출력을 제공하는데 사용(예를 들어 이진분류, 다중클래스 분류, 단순 회귀문제 등을 조절.)

<!-- 이미지 처리 과정을 확인하기 좋음 -->
https://setosa.io/ev/image-kernels 

<!-- 기본적인 내용은 유튜브에 -->
Neural Network By 3BlueBrown

Feed Forward NN의 중요점 및 한계
이 것의 반대는 순환신경망이 있음.
데이터의 독립변수간의 관계를 학습할 수 있다. 이는 데이터와 관련하여 중요하고 유용함.
- Learn relationships between independent variables in data
- supervised Learning
- data Compression : 피드포워드 신경망의 도움으로 수행
- Sonar Signal Recognition : 단반향 신호 송신 및 단방향 신호 수신인 소나 신호 인식이 있음. 루프가 없는 RNN과 달리 사용.
- Computer Vision : NLP의 경우 피드 포워드는 나쁨
- and many more

Types
- single layer perceptron
- multi layer 

한계
- Exploding and Vanishing Gradients
- Need large amount of data to converge
- Lots of parameters : 미세 조정하고 훈련하는데 많은 시간이 걸림.
  
순차 데이터와 관련해서는 매우 나쁨 시계열이나 NLP 등
은닉층 등 거대한 구조 때문에 exploding, vanshing problems 등이 있음. 그리고 매우 일반화된 모델을 갖기 위해서는 많은 양의 데이터가 필요하다. CNN과 비교하면 귀납적 편향이 있기에 이 편향은 매우 작은 데이터 세트에서는 특징을 얻는데유용하지만 피드포워드 신겸앙에는 귀ㅈ납적 편향이 없어 이 떄문에 모델이 보이지않는 데이터를 사용할 수 있도록 많은 양의 데이터가 필요.

CNN
1. What CNNs can do : 이미지 분류, 객체 탐지, 객체 분할(segmentation, 객체 탐지는 바운딩 박스로 하지만 객체 분할은 픽셀단위가 필요 Mask R-CNN, U0Net 등, 인스턴스 분할, 시맨틱 분할로 나뉨.), face recognition(아이폰 얼굴 잠금 등), image synthesis(이미지 합성, 데이터가 충분하지 않을 때 더 많은 데이터를 생성, 다른 유형으로는 GANs)
2. image classification : 이미지 분류는 어렵다. 왜냐하면 사람은 다른 관점에서 이해가 가능하지만 CNN은 조명이나 각도 등 부분에서 데이터 세트에 다양성이 중요하게 됨. 훈련 데이터 세트에 이런 종류의 다양성이 없으면 어려워 질 수 있음.
   - Traditional Approaches : 이는 수작업이 필요
     - Use hand-engineered features : 사람이 특징을 지정. 얼굴 인식에서 facial keypoints를 직접 지정.
     - Preprocess images(centering, cropping, etc.)

3. CNN Basics : 이는 수작업이 필요 없음.
    - CNN은 귀납적 편향[^1]이 있음. CNN에서 이 피처를 자동으로 찾음. Independence, Locality(객체 탐지에 사용), Sequentiality(RNN 등)
    - CNN 주요 개념
      - Sparse-connectivity : A single element in the feature map is connected to only a smoall pathc of pixles(this is very different from connection to the whole input image, in the case of MLP)
      - Parameter0sharing : The same weights are used for different pathces of the input images
      - Many layers : Combining extracted local patterrns to global patterns
  
4. convoluitional filters and weight-sharing
   - Weight Sharing : 가중치 공유는 변환 크기를 사용하여 마지막 이미지에서 정보 또는 픽셀 정보를 추출하는 것 다음 그 특정 가중치는 다른 작은 이미지에 임베드될 피쳐가 될것이다. CNN은 크기, 회전 및 변환에 대해 실제로 불변하지 않습니다. 회전으로 변경된 경우 예측하는데 어려움을 겪을 것입니다.
   

5. cross-corrrelation vs convolution
   
6. CNNs & Backpropagation
    Same overall concept as before: Multivariable chaine rule, but now with an additonal weight sharing constraint



RNNs
1. Sequental Modelling
   - Sequence Modeling : 순차적 데이터(X(t), X(t+1) 두 점은 연결된 데이터 유형)와, 순차적 모델링의 이해가 필요
   - Understanding RNNs
   - RNN variants
     - LSTM
     - GRU
     - Bi-directional sequence modelling
   - Challenges in vanilla RNNs

시퀀스 모델링 아키텍처가 필요한 정확한 이유는?
입력과 출력은 케이스마다 길이가 다를 수 있음. CNN이나 Fully connected layer들은 처음에 문장의 최대 길이를 가정하고 Padding을 추가하여 신경망을 초기화해야함. 이 패딩들은 분류 또는 localization에서 중요한 역할을 하지 않습니다. 따라서 이런한 것은 적절한 선택이 아니고 가변 길이 인코더, 가변길이 모델이 필요. 따라서 앞서 말한 두 모델은 적절하지 않음.

RNN
- perform well when the input data is interdependent in a sequental pattern
- Correlation between previous input to the next input
- Introduce bias based on your previous output
CNN
- ALL the outputs are self dependent
- Feed-forward nets don't rememver historic input data at test time unlike recurrent networks
  
RNN 
$h(t) = f_c(h(t-1), x(t))$, h(t) = new state, $f_c$= function with parameter c, h(t-1)=old state, x(t) input vector at time step t

- Provlems
  - Vanishing and exploding Gradient &rarr; LSTM이 해결, but take long time
  - Due to recurrent nature, RNNs take lots of time in training.


LSTM
- RNN short-term dependencies
- Basic LSTM
  - memory cell input : 마지막 셀에서 흭득한 정보와 특정 셀의 데이터
  - input gate : 새로 가져와야 하는 데이터
  - forget gate(self-recurrent connection) : 두가지 인풋으로 context[^2]가 변경되는데 안전을 위한 데이터로 기본적으로 두 데이터에서 정보를 분석하여 필요하지 않은 정보를 잊어버리게 함. 두가지 활성화 함수로 시그모이드, tanh 함수.
  - output gate : 
  - memory cell output
  - cell state: ht-1, ht, ht+1 노드 또는 라인을 명칭.
  - gate : 활성화 함수나 시그모이드 함수를 게이트라 부르고 대부분 시그모이드로 봄
- Step
  - forget gate : $f_t = \sigma(W_f \cdot [h_{t-1}m x_t] + b_f)$, 마지막 셀과 지금셀에서 중요하지 않은 정보를 잃음
  - input gate layer : 
    - $i_t = \sigma(W_i \cdot [h_{t-1}m x_t] + b_i)$, input state sigmoid 사용
    - $\tilde{C_t} = tanh(W_C \cdot [h_{t-1}m x_t] + b_C)$, cell state, tanh 사용
  - The current state : $C_t = f_t \ast C_{t-1} i_t \ast \tilde{C_t}$, 글로벌 컨텍스트 유지
  - output layer : 
    - $o_t = \sigma(W_o [h_{t-1}, x_t] + b_o)$
    - $h_t = o_t \ast tanh(C_t)$, 로컬 컨텍스트 정보, 현재 셀에서 얻은 정보.

Transformers : 가중 중요한 아키텍처 중 하나
- Attention : Attention is all you need
  - While processing **each word** it allows to look at other postions in the input sequence for clues to build a better encoding for **this word**
    - step1:create three vector
      - Query : 우리가 찾고 있는 단어에 관한 것. Wq
      - Key : 쿼리에 대한 키 Wk
      - Value : 키에 대한 값. Wv
      - 쿼리 임베딩에 따른 최적화된 키를 검색하고 최적화된 값을 검색하는 것
    - Step2: calculate a score
      - score : 특정 위치에 단어를 인코딩할 때 특정 문장 입력의 다른 부분에 얼마나 많은 초점이 맞춰졌는지 규칙적으로 주의를 기울였습니다. 여기에서 임베딩이 있고 쿼리, 키, 밸류가 있고 스코어가 있는데, 이 스코어는 쿼리와 키 이 두 행렬의 내적 곱셈. 스코어는 단 하나의 단어와 연결이 됨.
    - Step3 : 스코어를 키 벡터 차원의 제곱근으로 나누어 좀 더 안정적인 그래디언트를 얻음.
    - Step4 : 이 스코어에 softmax를 적용해 특정 단어의 확률을 얻음.
    - Step 5: intuition-softmax score determines how much each word will be expressed at this postion.
    - Step6 : 소프트 맥스 값 다음에 있는 가중치 벡터의 합. 특정 취잉에서 self-attention 레이어의 출력을 생성. 
    - More details : 
      - What we have seen for a word is done for all words(using matrices)
      - Need to encode position of words
      - And imporved using a 'multi-headed' attention
      - soruce : https://jalammar.github.io/illustrated-transformer/
  - self-attetion : 
    - $a^i = Wx^i$
    - query(to match others,$q^i = W^qa^i$)
    - key(to be matched,$k^i = W^qa^i$)
    - value(information to be extracted,$v^i = W^va^i$)
    - Scaled Dot-Product Attention:$\alpha_{1,i} = q^1 \cdot k^i/ \sqrt{d}$
    - soft-max : $\hat{\alpha_{1,i}} = exp(\alpha_{1,i})/\sum_j exp(\alpha_{1,i})$
    - $b^1 = \sum_j\alpha_{1,i}v^i$, considering the whole sequence, $b^i$ is obtained based on the whole input sequence.
  
  - multi-head attention(2-head example)
    - $q^{i,1} = W^{q,1}q^i$
    - $q^{i,2} = W^{q,2}q^i$ 
    - ...
    - $b^i = W^o {b^{i,1} \atop b^{i,2}}$
- Encoder Decoder
  - Positional Encoding 
    - self-attention에는 위치 정보가 없음.(타임스탬프)
    - Original paper : each postion has a unique postional vector $e^i$
    - in other words : each $x^i$ appends a one-hot vector $p^i$
- Transformers
  - 위의 내용들을 연결하여 사용.


> 2. RNN Models

One To Many
- intuition of One To Many : 입력 데이터는 하나의 시간 스텝이 있고 출력에는 여러 값 또는 여러 시간 스텝으로 구성된 벡터가 포함됨. 예이미지 캡션, 음악 생성, 감정 분석 
  - image captioning : CNN(이미지를 읽고 특정 이미지 임베딩) + RNN(CNN 임베딩은 RNN의 임베딩이 됨으로 RNN도 이미지도 학습함.)
- Many to one : 감정 분석 모델(Sentiment), 영화 평점, 음악 플레이리스트 추천(좋은 곡 선택의 흐름.)
- Many to Many
  - RNN for Sequence Input &rarr; Sequence Output
  - Output for the previous one becomes the input for the next one
  - Last sentences or words can be saved to serve for hte next step
  - CNN can't do such tasks
  - for Language Translation.

> 3. LSTM

순환 신경망은 NN의 하위 브랜치 모델로 표준 RNN, LSTM 및 GRU와 같은 알고리즘을 포

GRU
- Gated recurrent unit은 LSTM의 변형이며 LSTM은 기본적으로 RNN 기반으로 만들어짐.
- 인간의 두뇌는 정보의 흐름을 처리합니다. 대부분의 데이터는 순차적으로 취득되고, 사전처리 및 생성됩니다. 그래서 인간두뇌의 경우에처럼 우리는 음파와 인공지능을 취하게 됩니다. 그리고 어휘 또는 사전 또는 문장을 만들것입니다. 그리고 우리 인간은 같은 사고과정은 매우 지속적인 연결을 가지고있어 인간은 매 순간 처음부터 사고과정을가지지 않습니다. 그래서 우리는 이에 대해 마음속에 직관을 갖게 될 것입니다. 그것의 도움으로 우리는 새로운 정보를 가져올 것입니다. 이는 RNN 또는 Seq2Seqㅇ 문제의 예입니다. RNN은 가변 크기 입력을 처리할 수없는 CNN이나 다른 신경망과 다르게 처리가 가능하기 떄문.
- different between GUR and LSTM
  - GRU uses an update gate z to substitute the input and forget gates
  - conbined the cell state and gidden state in LSTM as a single cell state
  - GRU have 2 gate. so, more faster than LSTM
- Two recurrent cell desings were proposed and widly adopted:
  - reset gate : 시간 정보 캡처 역할, controls the composition of the new state
  - updated gate : 전역 시간 정보를 캡처하는 역할, determines how muchold information is needed in the alternative state
  - Alternative state : contains new information
  - New state : replace selected information with new information in the new state
- RNN의 가장 중요한 문제로 양방향 문제.
  - Bidirectional RNN
    - Connects two recurrent units of opposite directions to the same output
    - Captures forward and backward information from the input sequence
    - Apply to data whose current state can be better determined when given future information
  - NER(Named Entity Recognition) 문제.
  
> 4. Attention

- "Attention is all you need"
- 심리학적으로는 다른 것은 무시하면서 하나 또는 몇 가지에 선택적으로 집중하는 인지 과정
- 어텐션은 네트워크 아키텍처의 한 구 성요소로 상호 의존성을 관리하고 정량화하는 일을 담당  
  - Between the input and output elements(General Attention), 입력과 출력 요소 사이의 어텐션을 찾는 것
  - Within the input elements(self-attention), 입력요소의 중요성을 알아낼 때.
  - Step1: Encoder Hidden State, alignment score 계산
  - Step2: decoder input, encoder output tanh 함수에 전달.
  - Step3: Alignment, tanh 함수 결과 행렬 곱셈으로 Alignment Scores 얻음, 중요한 단어나 문장을 파악. 거대한 모델을 훈련핧 때 순서로 모든 것을 배우는 것이 실제로 실현 가능하지 않기 떄문에 무시할 수 있도록 실제로 필요하지 않은 정보를 찾는 것이 중요.
  - Step4: Step3의 결과를 softmax 함수로 전달하여 Attention Weights 얻음.
  - Step5: Encoder Outputs와 Attention Weights의 곱으로 COntext Vector를 얻음.
  - Step6: Context Vector와 Embedding of Previous Decoder Output을 활용 
- Types of Attention
  - Generalized Attention : 시퀀스에 대한 어텐션 매커니즘을 그래프 작업으로 생각하는 것. 그래프 이론으로 바꿈으로서 삭제된 쿼리, 키 및 밸류를 찾고 있음.
  - Self-Attention : 단일 시퀀스의 다른 위치를 가지고 동일한 시퀀스의 표현을 ㄱ싼하는 것.
    - RNN은 오래된 정보엑세스하는데 어려움이 있음.
  - Multi-HEad Attention : almost same Self-attention, 차이점은 셀프 어텐션은 헤드가 없지만 멀티 헤드 어텐션은 여러개의 헤드가 있음. 병렬로 여러번 실행되는 어텐션 매커니즘을 위한 모듈. 
  - Efficient Attention : 정확도의 손실 없이 quadratic에서 linear 어텐션 매커니즘의 계산 및 메모리 복잡성을 줄이는 간단하지만 효과적인 방법.
  - Attention Mask
    - 모델이 어텐션을 주지 않도록 패딩된 인덱스의 위치를 나타내는 바이너리 텐서.
    - 어텐션 마스크를 사용하는 주된 이유는 가변 길이 입력으로 모델을 미세 조정하는 경우 여기에 약간의 패딩이 필요합니다. 그런 다음 어텐션 마스크를 사용하여 중요하지 않다는 것을 모델에 알립니다.
  - Multi-head Attention
    - 어텐션 매커니즘을 병렬로 여러번 진행.
    - 

> 5. Transformers -> RNN 아키텍처로는 복잡성과 시간이 너무 길어서 그 문제를 해결.

- Encoder-Decoder 아키텍처
  - Goal : 문맥상 적절하게 임의 길이를 가진 출력 시퀀스를 생설할 수 있는 아키텍처를 개발하는 것. 응용 케이스는, 기계 번역, 요약, 질문 응답, ㄷ대화 모델링, 자동 완성 등.
  - Simple-RNN
    - Language Modeling
    - Sequence Classifcation(Sentiment, Topic)
    - Seq2Seq
    - 트랜스포머는 RNN을 보완하기 위해 나옴, 병렬 방식으로 훈련이 가능.
  - General Encoder Decoder Networks
    - Encoder : x 입력 시퀀스를 받고 인코더를 얻고 컨텍스트로 전달
    - Context vector C :  입력의 에센스를 디코더로 전달
    - Decoder : C를 입력으로 받아들이고 히든 스테이트의 임의 길이 시퀀스를 생성하고 이로부터 출력 스테이트 시퀀스를 얻을 수 있음.
- Transformers
  - https://jalammar.github.io/illustrated-transformer/
  - High-level architecture
    - Encoder : all identical in structure(not share weights). each one is broken down into two sub-layers(Feed Forward NN, Self-Attention)
    - key property of Transformer : word in each position flows through its own path in the encoder.
      - There are dependencies between these paths in the self-attention layer
      - Feed-forward layer does not have those dependencies &rarr; various paths can be executed in parallel
  - Positional Encoding
    - important concept
    - What is Positional Encoding? it's to keep track of the positions of the words
    - Why Positional Encoding? 트랜스포머 모델에는 모델이 시퀀스의 순서를 사용하기 위해 recurrence 및 convolution이 포함되어 있지 않습니다. RNN의 경우 전체 데이터를 순차적으로 전달하지만 트랜스포머의 경우에는 데이터를 병렬 방식으로 전달해 단어의 위치정보를 알아내는 것이 중요합니다. 시퀀스에서 토큰의 상대적 또는 절대 위치에 대한 정보를 주입해야합니다.(없다는 가정하 Tom bit a dog, A dog bit Tom은 트랜스포머 모델에서 같은 뜻으로 여겨짐)
      - 포지셔널 인코딩이 인코더 및 디코더 스택의 맨 아래에 있는 입력 임베딩이라고 함.
    - Why Element wise? 두 벡터의 연결을 사용하여 모델은 워드 임베딩으로 부터 독립적인 포지셔널 인코딩 벡터를 확인하므로 학습이 더 쉬워짐. 여기에 PE & WE Vector인 워드 임베딩 벡터 다음 포지셔널 인코딩 벡터가 있음. 벡터 방식으로 결합하면 위치 벡터를 갖게 됨. 그러나 이 두벡터를 요소별로 추가하면 모델이 더 쉽게 배울 수 있음.
    - How Positional Encoding works? Using of sine and cosine functions of different frequencis.
- BERT - Pre-training of Deep Bidirectional Transformers for Language Understanding
  - Pre-training in NLP : 구조화되지 않은 데이터 세트로 거대한 모델을 훈련. 그런 다음 프리 트레인된 모델을 사용하여 임베딩 및 워드 임베딩을 함.워드 임베딩은 NLP의 기초 과정.
    - Word embeddings(word2vec, GloVe) are often pre-traind on text corpus from co-occurrence statistics
    - Contextual Representations
      - Problme : Word embeddings are applied in a context free manner, 거대한 말뭉치와 하이레벨 차원에서 컨택스트 정보가 없음을 의미합니다.
      - Solution : Train contextual representations on text corpus, 텍스트 말뭉치에서 컨텍스트 표현을 학습시키는 것. 
    - Unidirectional context vs Bidirectional context
    - Masked LM : Mask out k% of the input words, and thenm predict the masked words
    - Next Sentence Prediction : To learn relationships between sentences, predict wheter Sentence B is actual sentence that proceeds Sentence A, or a random sentence
    - Inpuit Representation : in bert, have Position Embeddings, Segement Embeddings, Token Embeddings
    - Model Architecture
      - Multi-headed self attention
      - Feed-forward layers
      - Layer norm and residuals : Makes training deep networks healthy
      - Positional embeddings
    - Empirical advantages of Transformer vs, LSTM:
      - Self-attention == no locality bias : Long-distance context has "equal opportunity"
      - Single multiplication per layer == efficiency on TPU : Effective batch size is number of words, not sequences
    - Fine-Tuning Procedure : 마스크 언어 모델이나 마스킹 문제로 작업하는 경우 마스크를 문장으로 전달합니다. 여기서 우리는 마스킹된 문장 A와B를 전달합니다. 그런 다음 여기에 출력 임베등을 갖게 됩니다. 
- GPT - OpenAI에서 도입한 언어 모델, 트랜스포머 디코더 스택.
  - GPT have self-attention, BERT have Masked Self-Attention
  - GPT-2는 큰 모델이라 저 사양 시스템에서 트레인하는 것은 쉽지 않다.
  - 언어 모델을 훈련하는 비지도 학습 방법, BERT처럼 프리 트레이닝이나 미세 조정을 분리하지 않음. 따라서 다시 훈련시킬 필요가 없음. 충분히 훈련되어 있음. 그러나 BERT는 자신의 문제에 대한 자신만의 경로를 찾아야 함.
  - Translation, Summarization 등의 방안이 있음.
- Bloom
  - GPT가 오픈소스 모델이 아니므로 GPT 이후 가장 중요한 언어 모델, 그러나 Bloom은 오프소스 언어 모델.
  - What is Bloom? - https://huggingface.co/docs/transformers/model_doc/bloom


> 6. Transformer 실습

- Zero Shot Classification(ZSC)
  - What is ZSC? - 다른 클래스에 대한 사전 교육이나 지식 없이 이미지와 테스트를 여러 범주 중 하나로 분류하는 작업. 다름 아닌 기본적인 머신러닝 패러다임. 사전 훈련된 딥러닝 모델은 새로운 샘플의 범주를 일반화하도록 만들어졌다는 것을 알고 있습니다. Zero-Shot 학습의 경우 지도 학습 임베딩 러너의 지식을 Zero0Shot 러너로 이전하는 입니다.
  - 

- MIMO(Multi input and Multi Ouput)



[^1]: 개개인의 구체적인 사실이나 현상에 대해 관찰로서 얻어진 인식을 전체에 대한 일반적인 인슥으로 이끌어나가는 절차
[^2]: 문맥, 맥락