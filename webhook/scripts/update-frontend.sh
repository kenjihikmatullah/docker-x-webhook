#!/bin/bash

cd ../frontend
git pull

docker exec dxw-frontend npm run build