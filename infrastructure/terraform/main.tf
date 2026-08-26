resource "docker_image" "sentinel" {

  name = "sentinel-data:latest"

  build {

    context = "../.."

    dockerfile = "docker/Dockerfile"
  }
}


resource "docker_container" "sentinel_api" {

  name = "sentinel-api"

  image = docker_image.sentinel.image_id

  ports {

    internal = 8000

    external = 8000
  }

  env = [

    "APP_ENV=production"
  ]
}