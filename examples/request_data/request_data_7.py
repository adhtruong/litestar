from starlite import Body, MediaType, RequestEncodingType, Starlite, UploadFile, post


@post(path="/", media_type=MediaType.TEXT)
def handle_file_upload(
    data: UploadFile = Body(media_type=RequestEncodingType.MULTI_PART),
) -> str:
    content = data.file.read()
    filename = data.filename
    return f"{filename}, {content.decode()}"


app = Starlite(route_handlers=[handle_file_upload])
