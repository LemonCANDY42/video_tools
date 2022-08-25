# ffmpeg on M1 Mac with GPU



### H.264 to H.265

```shell
ffmpeg -hwaccel videotoolbox -i 历山舜王坪-姥姥_264.mp4 -c:v hevc_videotoolbox -b:v 5M -tag:v hvc1 -c:a eac3  历山舜王坪_姥姥_265.mp4
```

### extract frames

```shell
ffmpeg -i input.mp4 -filter:v fps=fps=1/360 img/ffmpeg_%0d.jpg
```