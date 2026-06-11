# API 명세
- APIKEY = 실제 임베디드 기기에만 삽입되는 키

## 분실물 등록
- POST /api/v1/lost
	- apikey
	- image
	- context
- response
	- status
	- data
		- id
		- context

## 분실물 삭제
- DELETE /api/v1/lost/:id
	- apikey (header)
- response
	- status

## 분실물 목록
- GET /api/v1/lost
- response
	- data:list
		- imagelink
		- context
		- created-at
		- id
 
## db
- sql 확인 필요
