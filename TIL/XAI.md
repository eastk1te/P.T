
> ## XAI(Explainable Artificial Intlligence)

XAI란?
: 해석 가능한 인공지능으로 기계학습 모델이 내린 결정 또는 예측을 이해하고 설명할 수 있는 방법을 개발하는 분야입니다. 블랙박스 문제를 해결하기 위해 다양한 기술과 접근 방식을 사용.

- 피쳐 중요도 분석 - 모델이 예측에 어떤 피쳐를 중요하게 여기는지 확인합니다. 랜덤 포레스트의 경우 트리 구조를 분석하여 피처 중요도를 계산
- 로컬 해석 - 예측에 영향을 미치는 특징과 패턴을 설명. LIME은 모델의 ㅇ측을 해석하기 위해 해당 예측 주변의 데이터를 사용하여 해석 가능한 모델을 만듭니다/
- 그래프 기반 설명 - 모델이 어떻게 의사결정을 내리는지 시각적으로 표현. 트리 구조를 시각화하여 모델의 동작을 이애할 수 있음
- 예시 기반 설명 - 특정 예시를 선택하고 해당 예씨에 대한 모델의 의사결정 근거를 제공합니다. SHAP는 기댓값적 도움을 통해 모델 예측을 설명합니다.

LIME (Local Interpretable Model-agnostic Explanations):

LIME provides local interpretability by approximating a complex model's behavior with a simpler interpretable model (e.g., linear model).
It generates perturbed instances around a specific prediction and observes how the interpretable model's predictions change.
Library: The lime library in Python offers an implementation of LIME for various models.
SHAP (Shapley Additive exPlanations):

SHAP explains the contribution of each feature to a prediction by computing Shapley values from cooperative game theory.
It considers all possible feature combinations and determines the importance of each feature by evaluating their impact on predictions.
Libraries: The shap library in Python provides an implementation of SHAP for interpreting models.
Integrated Gradients:

Integrated Gradients explains predictions by computing the integral of the gradients of the model's output with respect to the input features.
It assigns importance to features based on how they contribute to changes in predictions.
Libraries: The captum library in PyTorch and the interpret library in TensorFlow offer implementations of Integrated Gradients.
Decision Trees and Rule-based Explanations:

Decision trees are inherently interpretable models that represent a sequence of rules for making predictions.
They provide explicit paths of decisions, enabling easy interpretation of model behavior.
Libraries: Scikit-learn (sklearn) in Python provides decision tree algorithms for building interpretable models.
Rule Extraction from Neural Networks:

Rule extraction techniques aim to extract human-readable rules from complex neural networks.
These rules can provide insights into the decision-making process of the model.
Libraries: Tools such as LEMNADE, LORRI, or Zennit provide rule extraction capabilities for neural networks.
Model-agnostic Libraries:

Some libraries provide model-agnostic approaches for explaining machine learning models. They can work with a wide range of models without requiring specific implementations for each model type.
Libraries: Libraries such as eli5, skater, and alibi offer model-agnostic techniques like feature importance analysis, partial dependence plots, and rule-based explanations.
