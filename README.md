# Django CI/CD Mini Project

A tiny Django application designed to practice a GitHub Actions CI/CD pipeline.

## Pipeline

GitHub push/PR
-> Checkout
-> Setup Python
-> Install dependencies
-> Run tests
-> Build Docker image

## Run locally without Docker

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
python manage.py test
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Run with Docker

```bash
docker build -t cicd-demo .
docker run --rm -p 8000:8000 cicd-demo
```

Open http://localhost:8000/

Or:

```bash
docker compose up --build
```

## GitHub setup

1. Create a new GitHub repository.
2. Copy these files into it.
3. Commit and push to the `main` branch.
4. Open the repository's Actions tab.
5. The workflow in `.github/workflows/ci-cd.yml` should start automatically.

## Optional Docker Hub CD

The current workflow intentionally uses `push: false`, so it only builds the image.

To push to Docker Hub later, add these GitHub repository secrets:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

Then change the Docker build step to:

```yaml
- name: Login to Docker Hub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKERHUB_USERNAME }}
    password: ${{ secrets.DOCKERHUB_TOKEN }}

- name: Build and Push Docker image
  uses: docker/build-push-action@v6
  with:
    context: .
    file: ./Dockerfile
    push: true
    tags: ${{ secrets.DOCKERHUB_USERNAME }}/cicd-demo:latest
```

This gives you a simple CI -> Docker image -> Docker Hub CD flow.
