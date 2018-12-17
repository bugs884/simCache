#!/bin/bash
./sim-cache -redir:sim results/log_F1.out -cache:dl1  mycache:1024:8:1:l benchmarks/fibonacci &
./sim-cache -redir:sim results/log_F2.out -cache:dl1  mycache:2048:8:1:l benchmarks/fibonacci &
./sim-cache -redir:sim results/log_F3.out -cache:dl1  mycache:4096:8:1:l benchmarks/fibonacci &
./sim-cache -redir:sim results/log_F4.out -cache:dl1  mycache:8192:8:1:l benchmarks/fibonacci &
./sim-cache -redir:sim results/log_F5.out -cache:dl1  mycache:16384:8:1:l benchmarks/fibonacci &
./sim-cache -redir:sim results/log_F6.out -cache:dl1  mycache:32768:8:1:l benchmarks/fibonacci &
./sim-cache -redir:sim results/log_F7.out -cache:dl1  mycache:65536:8:1:l benchmarks/fibonacci &
./sim-cache -redir:sim results/log_F8.out -cache:dl1  mycache:131072:8:1:l benchmarks/fibonacci 










