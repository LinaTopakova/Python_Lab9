FROM python:3.12-slim
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/.venv /app/.venv
COPY ./app ./app
COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x entrypoint.sh

ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8000
CMD ["./entrypoint.sh"]