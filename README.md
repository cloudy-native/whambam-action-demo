# whambam GitHub Action demo

A tiny API (`app.py`) whose pull requests are load-tested with
[whambam](https://whambam.dev), using its GitHub Action:

```yaml
- uses: cloudy-native/whambam.dev@v1
  with:
    url: http://127.0.0.1:8002/
    args: -z 20s -c 10 --qps 200
    baseline: baseline.json
    assert: p99<+25%,errors<1%
```

[`.github/workflows/load-test.yml`](.github/workflows/load-test.yml) starts `main` and the pull request side by
side on the runner, measures `main` as the baseline, then fails the check if the pull request makes p99
latency more than 25% worse. Open pull requests show it passing and failing.

Run the app yourself: `python3 app.py 8000`, then `whambam http://127.0.0.1:8000/ -z 10s`.

MIT licensed.
