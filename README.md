# DevSecOps Demo

A small Python HTTP service for demonstrating a two-entry DevSecOps workflow.

## Run locally

```bash
python3 -m app.server
```

Then open `http://127.0.0.1:8080/health`.

## Test

```bash
python3 -m unittest discover -v
```

## Container

```bash
docker build -t devsecops-demo .
docker run --rm -p 8080:8080 devsecops-demo
```

The repository includes:

- `azure-pipelines.yml` for Azure DevOps Pipelines
- `.github/workflows/ci.yml` for GitHub Actions
- `k8s/` starter manifests for the later GitOps phase