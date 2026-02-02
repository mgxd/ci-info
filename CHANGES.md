0.4.0 (February 2, 2026)
========================
- Enable is_pr detection for AWS CodeBuild, Appcircle, and Vercel
- Add new CI providers:
    Agola CI, Cloudflare Pages, Cloudflare Workers, Earthly CI,
    Gerrit CI, Gitea Actions, Google Cloud Build, Harness CI,
    Heroku, Prow, ReleaseHub, Sourcehut, Vela, and Woodpecker

0.3.0 (July 27, 2022)
=====================
Adds CI detection for:

-Appcircle
-Codefresh
-Expo Application Services
-Github Actions
-LayerCI
-Render
-Screwdriver
-Vercel
-Visual Studio App Center

Additionally, drops support for Python 3.5 and 3.6, as they are now EOL.

0.2.0 (April 16, 2020)
======================

- Renamed package import to `ci_info`
- Added tests for Circle CI.