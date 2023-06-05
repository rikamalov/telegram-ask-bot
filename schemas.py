from pydantic import BaseModel, Field

class Chat(BaseModel):
    id: int
    first_name: str = None
    last_name: str = None
    username: str = None
    type: str

class Photo(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: int
    width: int
    height: int


class FromF(BaseModel):
    chat_id: int = Field(alias='id')
    is_bot: bool
    first_name: str
    last_name: str = None
    username: str = None
    language_code: str = None

class Thumb(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: int
    width: int
    height: int

class Document(BaseModel):
    file_name: str
    mime_type: str
    thumb: Thumb = None
    file_id: str
    file_unique_id: str
    file_size: int


class Video(BaseModel):
    duration: int
    width: int
    height: int
    file_name: str
    mime_type: str
    thumb: Thumb = None
    file_id: str
    file_unique_id: str
    file_size: int

class Animation(BaseModel):
    file_name: str
    mime_type: str
    duration: int
    width: int
    height: int
    thumb: Thumb = None
    file_id: str
    file_unique_id: str
    file_size: int


class Location(BaseModel):
    latitude: float
    longitude: float


class Audio(BaseModel):
    duration: int | float
    file_name: str
    mime_type: str
    title: str
    performer: str
    file_id: str
    file_unique_id: str
    file_size: int


class Voice(BaseModel):
    duration: int | float
    mime_type: str
    file_id: str
    file_unique_id: str
    file_size: int

class ReplayMessage(BaseModel):
    message_id: int
    fromF: FromF = Field(alias='from')
    chat: Chat
    date: int
    text: str = None
    photo: list[Photo] = None
    document: Document = None
    video: Video = None
    caption: str = None
    forward_from: FromF = None
    forward_date: int = None
    entities: list = None
    caption_entities: list = None
    media_group_id: int = None # если это группа фотографий, приходят они двумя разными запросами, но это айди один.
    animation: Animation = None # если это гифка пришла, как документ но с указанием анимации
    location: Location = None # обработка локации в сообщении, обычно больше ничего и нет, но всё возможно
    audio: Audio = None # обработка песен
    voice: Voice = None # обработка голосового сообщения


class Message(BaseModel):
    message_id: int
    from_f: FromF = Field(alias='from')
    chat: Chat
    date: int
    text: str = None
    photo: list[Photo] = None
    document: Document = None
    video: Video = None
    caption: str = None
    sticker: dict = None # возможно и не нужно
    forward_from: FromF = None
    forward_date: int = None
    entities: list = None
    caption_entities: list = None
    media_group_id: int = None # если это группа фотографий, приходят они двумя разными запросами, но это айди один.
    animation: Animation = None # если это гифка пришла, как документ но с указанием анимации
    location: Location = None # обработка локации в сообщении, обычно больше ничего и нет, но всё возможно
    audio: Audio = None # обработка песен
    voice: Voice = None # обработка голосового сообщения
    reply_to_message: ReplayMessage = None


class Answer(BaseModel):
    update_id: int
    message: Message
