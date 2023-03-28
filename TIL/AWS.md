### AWS
|     |    |
| --- |--- |
| Athena | SQL로 S3에 있는 데이터 간편하게 분석 가능한 대화형 쿼리 서비스 |
| DynamoDB | 완전 관리형 NoSQL(수평적) DB service |
| EBS | 대규모 고성능 스토리지 | 
| EC2 | Elastic compute cloud 가상서버 | 
| RDS | 관계형 DB, 확장성 있는 DB 제공 |
| VPC | 독립(폐쇄) 가상 네트워크, DNS, routes 설정으로 외부와 통신 |
| CloudFormation | 인프라 관리 간소화 |
| KMS | key management service, 암호화키 생성 및 제어 |
| Lambda | sever less computing platform | 
| SDK(Software Development Kit) | 하드웨어 플랫폼, 운영 체제(OS) 또는 프로그래밍 언어 제작사가 제공하는 일련의 툴 | Flutter(GUI 애플리케이션 프레임워크)
| S3 | data lake|
|figma | web 기반 그래픽 편집기 | 
| Software Development Kit | |

```python
### AWS로 sever operation
 - SSH : private key, need SSH terminal program

IaC : 코드형 인프라, 장점 : 속도향상, 안정성 향상, 구성 드리프트 방지, 실험,테스트 및 최적화 지원
Terraform : IaC tool, use .tf script


# S3 storage를 위한 boto3 : https://gaussian37.github.io/python-etc-s3_storage_for_boto3/
# boto3 : https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
# Terraform : https://www.ibm.com/kr-ko/cloud/learn/terraform#toc-terraform--1LqmX9x5
# Terraform : https://techblog.woowahan.com/2646/
# jenkins : https://ict-nroo.tistory.com/31
# Amazon EKS : https://aws.amazon.com/ko/eks/faqs/
# the red 추천알고리즘
# 오케스트레이션

# About lambda :  https://seoyeonhwng.medium.com/aws-lambda%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-44df535d5487


# ECR(EC2 container registry) | docker container의 image를 저장하는 repository 서비스
# docker | image들을 모을 수 있는 OS환경
# image | .exe 파일 같은 개념

```