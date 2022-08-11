
docker run -it --rm \
  -v $(pwd):/root/src/app \
  -p 8001:8001 \
  --name myflaskapp \
  --network app-dev \
  myflaskapp \
  /bin/bash
