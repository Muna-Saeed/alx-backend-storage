# 0x02. Redis basic

# Redis Basic

This repository contains Python scripts for implementing basic Redis operations, such as caching and tracking web requests.

## Description

- `exercise.py`: Contains the implementation of basic Redis operations including storing data, retrieving data, counting calls, storing lists, and retrieving lists.
- `web.py`: Implements an expiring web cache and tracker using Redis. It includes a function to fetch the HTML content of a URL, cache the result with an expiration time of 10 seconds, and track how many times each URL is accessed.

## Requirements

- Python 3.7
- Redis server
- Redis Python client
- Dependencies: `redis`, `requests`

## Installation

1. Install Redis server:
    ```sh
    sudo apt-get -y install redis-server
    ```

2. Install Redis Python client:
    ```sh
    pip3 install redis
    ```

3. Modify Redis configuration to bind to localhost:
    ```sh
    sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
    ```

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/Muna-Saeed/alx-backend-storage.git
    ```

2. Navigate to the project directory:
    ```sh
    cd 0x02-redis_basic
    ```

3. Run the desired Python script:
    ```sh
    python3 exercise.py
    python3 web.py
    ```

## Credits

This project was created by [ME](Muna Saeed).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
