# diet-tracker 프로젝트 설정

## 배포

- GitHub Pages로 배포됩니다 (`origin` = `wkdckdgur5-a11y/diet-tracker`, `main` 브랜치, `index.html`이 사이트 루트).
- 라이브 URL: `https://wkdckdgur5-a11y.github.io/diet-tracker/`
- `sw.js`(서비스워커)가 캐싱하므로, 배포 후 폰 등 이미 방문한 기기에서는 앱을 완전히 껐다 켜야 최신 버전이 보일 수 있습니다.

## Git 워크플로

- **커밋 후 매번 push 승인을 묻지 않고, commit과 push를 한 번에 진행합니다.** (사용자가 2026-08-11 명시적으로 요청한 표준 워크플로)
- `git push`가 인증 GUI 팝업 대기로 멎는 경우가 있음 → `GIT_TERMINAL_PROMPT=0 timeout 20 git push origin main` 형태로 실행하면 저장된 자격 증명을 바로 사용해 멎지 않고 성공함 (2026-08-11 확인). 새 컴퓨터라면 먼저 GitHub Desktop 등으로 한 번 로그인해서 자격 증명을 저장해둬야 이 방식이 통합니다.
- push 후에는 실제 GitHub Pages 라이브 URL에서 반영 여부를 curl 등으로 확인합니다.
- 단, 아래 상황은 예외로 항상 먼저 확인합니다:
  - `git push --force` 등 강제 push
  - `main`이 아닌 다른 브랜치로의 push, 또는 브랜치/원격 설정 변경
  - 커밋 내용에 시크릿/토큰으로 보이는 문자열이 포함된 경우

## 배경

`project-brief.md`에 사용자 프로필, 12주 운동 프로그램, 식단 원칙 등 이 앱의 기획 배경이 정리되어 있습니다.
