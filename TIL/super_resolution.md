
> ## Super Resolution

Super resolution이란?
: 저해상도 영상을 고해상도 영상으로 변환하는 작업.(이하 SR)

학습의 어려움.
하나의 저해상도 이미지에 여러 개의 고해상도 이미지가 나올 수 있음.
SR문제의 복잡도. 전량적 평가와 정성적 평가가 일치하지 않을 수 있음.

평가 방법
MSE - 
PSNR - peak-signal-to-noise ratio 영상 내 신호가 가질 수 있는 최대 신호에 대한 잡음의 비율. 영상을 압축했을 때 화질이 얼마나 손실되었는지 평가하는 목적
SSIM - Structural similarity index map : 구조적 유사도를 평가 즉, 인간의 시각적 화질 차이를 평가하기 위해 고안된 방법으로 이미지 구조 정보를 도출하는데 특화됨. Luminance(휘도), Contrast(대비), Strucctural(구조) 3가지 측면에서 품질을 평가.

즉 PSNR은 정량적 평가로 SSIM 정성적 평가로 두 점수 모두 높아야 좋다. 

[연관 페이지](https://github.com/eastk1te/Patch_based_synthesis)
