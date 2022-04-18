FROM julianbei/alpine-opencv-microimage:p3-3.1

RUN apk update && apk upgrade
RUN mkdir ai-app && cd ai-app
COPY .  ai-app/
