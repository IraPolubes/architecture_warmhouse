FROM golang:1.22 AS builder

WORKDIR /app

ENV GOPROXY=direct
ENV GOSUMDB=off

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o smarthome

FROM debian:bookworm-slim

WORKDIR /app
COPY --from=builder /app/smarthome .

EXPOSE 8080
CMD ["./smarthome"]