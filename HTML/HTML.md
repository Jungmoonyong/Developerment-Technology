---
title: HTML Basic Syntax
date: 2021-12-06 11:51:05
tags: Technology
category: Technology
---

## HTML

### Head
웹 페이지의 정보, 문서에서 사용할 외부 파일들을 링크할 때 사용합니다
### Body
브라우저에 실제 표시되는 내용을 담고있습니다

### Br Tag
줄바꿈을 할 수 있습니다

```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    Hello<br>
    Hello
</body>
</html>
```

### P Tag
문단을 만들때 사용합니다

```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <p>First Paragraph</p>
    <p>Second Paragraph</p>
</body>
</html>
```

### B Tag
글자를 굵게 표시할때 사용합니다

```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <b>B Tag</b>
</body>
</html>
```

### I Tag
글자를 기울일때 사용합니다

```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <i>I Tag</i>
</body>
</html>
```

### H# Tag
문단의 제목을 나타내며 숫자가 작을수록 크기가 커집니다.

```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <h1>H1 Tag</h1>
    <h2>H2 Tag</h2>
    <h3>H3 Tag</h3>
</body>
</html>
```

### A Tag
링크를 걸어줄 수 있습니다

- href : 클릭시 이동 할 링크
- target : 링크를 여는 방법
  - _self : 현재 페이지
  - _blank : 새 탭
  - _parent : 부모페이지로 iframe 등에서 사용
  - _top : 최상위 페이지로 iframe 등에서 사용

```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <a href='https://naver.com'>naver</a>
</body>
</html>
```

### Img Tag
이미지를 삽입할 수 있습니다

```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <img src=~ width='245' height='50'>
</body>
</html>
```

### Iframe Tag
현재 HTML 문서에 다른 문서를 포함시킬 때 사용합니다

```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title>test</title>
</head>
<body>
    <iframe src="~" title=""></iframe>
</body>
</html>
```

### Table Tag
표를 만들 수 있습니다

- tr 태그는 표의 행을 타나냄
- td 태그는 표의 열을 나타내며 tr , td 등의 태그와 같이 작성

```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <table>
        <tr>
            <td>1</td>
            <td>2</td>
        </tr>
        <tr>
            <td>3</td>
            <td>4</td>
        </tr>
    </table>
</body>
</html>
```

### Div Tag
레이아웃을 나누는데 사용합니다

```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div style="background-color:cyan">1</div>
    <div style="width:100px; height:100px; background-color:#CF0">2</div>
</body>
</html>
```

### Span Tag
Div 와 같이 CSS 와 사용되지만 Div 는 줄바꿈이 되고 Span 은 안됩니다

```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <span style="background-color:red">1</span>
	<span style="background-color:blue">2</span>
	<span style="background-color:green">3</span>
</body>
</html>
```

### Li Tag
목록을 만들 수 있습니다

- ol 태그는 번호를 메겨 순서가 있는 목록을 만듬
- ul 태그는 순서없이 모양으로 목록을 만듬

```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <ol>
        <li>1</li>
        <li>2</li>
    </ol>

    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <ol>
            <li>3-1</li>
            <li>3-2</li>
        </ol>
    </ul>
</body>
</html>
```

### Form Tag
입력 양식을 만드는데 사용합니다

- name : 폼의 이름
- action : 폼 데이터가 전송되는 백엔드 URL
- method : 폼 전송 방식

```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <form>
        <p>
            <strong>아이디</strong>
            <input type="text" name="name" value="아이디 입력">
        </p>
        <p>
            <strong>비밀번호</strong>
            <input type="password" name="password" value="비밀번호 입력">
        </p>
        <p>
            <strong>성별</strong>
            <input type="radio" name="gender" value="M">남자
            <input type="radio" name="gender" value="F">여자
        </p>
        <p>
            <strong>응시분야</strong>
            <input type="checkbox" name="part" value="eng">영어
            <input type="checkbox" name="part" value="math">수학
        </p>
        <p>
            <input type="submit" value="제출">
        </p>
    </form>
</body>
</html>
```

### Title Tag
```html
<!DOCTYPE html>
<html lang = 'ko'>
<head>
    <meta charset="UTF-8">
    <title>test</title>
</head>
<body>
</body>
</html>
```

### Input Tag
양식을 입력하기 위해 사용합니다
type 속성을 통해 종류를 나타내며 name을 통해 데이터의 이름 value를 통해 기본 값을 지정합니다

- text: 일반 문자
- password: 비밀번호
- button: 버튼
- submit: 양식 제출용 버튼
- reset: 양식 초기화용 버튼
- radio: 한개만 선택할 수 있는 컴포넌트
- checkbox: 다수를 선택할 수 있는 컴포넌트
- file: 파일 업로드
- hidden: 사용자에게 보이지 않는 숨은 요소

* * *

## Reference

[HTML 기초 내용 정리](https://velog.io/@ljinsk3/HTML-%EA%B8%B0%EC%B4%88-%EB%82%B4%EC%9A%A9-%EC%A0%95%EB%A6%AC)
[HTML 입문](https://ofcourse.kr/html-course/HTML-%EC%9E%85%EB%AC%B8)
