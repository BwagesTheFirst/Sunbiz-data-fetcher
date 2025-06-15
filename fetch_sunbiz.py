  name: Fetch SunBiz Data
  on: [push]
  jobs:
    fetch:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - run: python fetch_sunbiz.py
