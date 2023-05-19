const peaky_play_pause = document.querySelector(".play-pause_button")
const video = document.querySelector("video")
const videodiv = document.querySelector(".player")
const full_screen = document.querySelector(".full_screen")
const mini_player = document.querySelector(".mini_player")
const volumediv = document.querySelector(".volume")
const volume_range = document.querySelector(".volume_range")
const time = document.querySelector(".duration_div")
const end_time = document.querySelector(".end_time")
const start_time = document.querySelector(".start_time")
const controls = document.querySelector(".controls")
const controls_div = document.querySelector(".controls_div")
const subtitres = document.querySelector(".subtitres")
const speed = document.querySelector(".speed")
const preview = document.querySelector(".preview")
const thumbnail = document.querySelector(".thumb_indicator")
const timeline_div = document.querySelector(".timeline_div")
const next_series1 = document.querySelector(".next_button1")
const next_series2 = document.querySelector(".next_button2")
var button_series = document.querySelectorAll(".button_serias")
const preview_time = document.querySelector(".preview-time")

document.addEventListener("keydown", e => {
    const tagname = document.activeElement.tagName.toLowerCase()

    if (tagname == "input") return

    switch(e.key.toLowerCase()){
        case " ":
            if (tagname === "button") return
        case "k":
            toggleplay()
            break
        case "f":
            togglefull()
            break
        case "i":
            togglemini()
            break
        case "m":
            togglevolume()
            break
        case "arrowleft":
            skip(-5)
            break    
        case "arrowright":
            skip(5)
            break
        case "arrowdown":
            volume_set(-0.1)
            break
        case "arrowup":
            volume_set(0.1)
            break
    }
})
video.addEventListener("dblclick", togglefull)
var A;
console.log(A)
timeline_div.addEventListener("mouseout", () => {
    start_time.textContent = formatDuration(video.currentTime)
    A = 1
})

timeline_div.addEventListener("mouseover", () => {
    A = 0
    console.log(A)
});

video.addEventListener("timeupdate", () => {
    if (A === 0){
        console.log("Вишоооов")
    }else{
        start_time.textContent = formatDuration(video.currentTime)
    }
    const percent = video.currentTime / video.duration
    timeline_div.style.setProperty("--progress-position", percent)
})

timeline_div.addEventListener("mousemove", handletime)
timeline_div.addEventListener("mousedown", toggleScrubbing)
document.addEventListener("mouseup", e => {
    if (isScrubbing) toggleScrubbing(e)
})
document.addEventListener("mousemove", e => {
    if (isScrubbing) handletime(e)
})

let isScrubbing = false
let wasPaused
function toggleScrubbing(e){
    const rect = timeline_div.getBoundingClientRect()
    const percent = Math.min(Math.max(0, e.x - rect.x), rect.width) / rect.width
    isScrubbing = (e.buttons & 1) === 1
    videodiv.classList.toggle("scrubbing", isScrubbing)
    if (isScrubbing){
        wasPaused = video.paused
        video.pause()
    }else{
        video.currentTime = percent * video.duration
        if (!wasPaused) video.play()
    }
    handletime(e)
}

function handletime(e) {
    const rect = timeline_div.getBoundingClientRect()
    const percent = Math.min(Math.max(0, e.x - rect.x), rect.width) / rect.width

    const time = percent * video.duration;
    preview_time.textContent = formatDuration(time)

    timeline_div.style.setProperty("--preview-position", percent)

    if(isScrubbing){
        e.preventDefault()
        timeline_div.style.setProperty("--progress-position", percent)
    }
}

speed.addEventListener("click", togglespeed)

function togglespeed(){
    let speedplay = video.playbackRate + .25
    if (speedplay > 2) speedplay =.25
    video.playbackRate = speedplay
    speed.textContent = `${speedplay}x`
}

function toggleplay(){
    video.paused ? video.play() : video.pause()
}
video.addEventListener("play", () => {
    videodiv.classList.remove("paused")
})
video.addEventListener("pause", () => {
    videodiv.classList.add("paused")
})

full_screen.addEventListener("click", togglefull)
mini_player.addEventListener("click", togglemini)

function togglefull (){
    if (document.fullscreenElement === null){
        videodiv.requestFullscreen()
    }else{
        document.exitFullscreen()
    }
}

function togglemini (){
    if (video.classList.contains("mini-player")){
        document.exitPictureInPicture()
    }else{
        video.requestPictureInPicture()
    }
}

document.addEventListener("fullscreenchange", () => {
    videodiv.classList.toggle("full_screen", document.fullscreenElement)
    console.log("Дааа")
})

peaky_play_pause.addEventListener("click", toggleplay)
video.addEventListener("click", toggleplay)

video.addEventListener("enterpictureinpicture", () => {
    videodiv.classList.add("mini_player")
})
video.addEventListener("leavepictureinpicture", () => {
    videodiv.classList.remove("mini_player")
})

volumediv.addEventListener("click", togglevolume)
volume_range.addEventListener("input", e => {
    video.volume = e.target.value
    video.muted = e.target.value === 0
})

function togglevolume() {
    video.muted = !video.muted
}

video.addEventListener("volumechange", () => {
    volume_range.value = video.volume
    console.log(volume_range.value)
    let volumelevel
    if (video.muted || video.volume == 0){
        volume_range.value = 0
        volumelevel = "muted"
        console.log("000000000000000")
    } else if (video.volume >= 0.5) {
        volumelevel = "high"
        console.log("05555555")
    } else {
        volumelevel = "low"
    }

    videodiv.dataset.volumelevel = volumelevel
})

video.addEventListener("loadeddata", () => {
    end_time.textContent = formatDuration(video.duration)
})


const learnzero = new Intl.NumberFormat(undefined, {
    minimumIntegerDigits: 2
})

function volume_set(count) {
    video.volume += count
}

function formatDuration(time){
    const sec = Math.floor(time % 60)
    const minuts = Math.floor(time / 60 ) % 60
    const hours = Math.floor(time / 3600)
    if (hours === 0) {
        return `${minuts}:${learnzero.format(sec)}`
    }else{
        return `${hours}:${learnzero.format(
            minuts
            )}:${learnzero.format(sec)}`
    }
}

function skip(seconds) {
    video.currentTime += seconds
}
document.addEventListener("fullscreenchange", function() {
    if (document.fullscreenElement) {
        setTimeout(function(){
            for(var i = 0; i < 3; i++){
                controls.style.display = "none";
                controls.style.cursor = "none";
            }
        }, 3000)
    }else{
        controls.style.display = "flex";
    }
});

var timeout = setTimeout(hideControls, 3000);

// Добавляем обработчик событий на движение мыши и нажатие клавиш на клавиатуре
document.addEventListener('mousemove', resetTimeout);
document.addEventListener('keypress', resetTimeout);

// Функция для скрытия элементов управления видео
function hideControls() {
  timeline_div.style.display = 'none';
  controls.style.display = 'none';
  video.style.cursor = "none";
  controls.style.cursor = "auto";
}

// Функция для показа элементов управления видео
function showControls() {
 timeline_div.style.display = "flex";
 controls.style.display = "flex";
 video.style.cursor = "auto";
 controls.style.cursor = "auto";
 controls_div.style.background = "linear-gradient(to top, rgba(0, 0, 0, .75), transparent)";
}

// Функция для сброса таймера
function resetTimeout() {
  clearTimeout(timeout);
  showControls();
  timeout = setTimeout(hideControls, 3000);
}

//next_series1.addEventListener("click", () => {
//    video.src = "images/peaky_video.mp4"
//})
//next_series2.addEventListener("click", () => {
//    video.src = "images/video.mp4"
//})

button_series.forEach(function(button){
    button.addEventListener("click", function(){
        video.src = this.dataset.src;
        video.pause()
        videodiv.classList.add("paused")
    })
})

