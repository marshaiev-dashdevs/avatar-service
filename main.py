from avatar_manager import AvatarManager
from avatar_searcher_service.mock import MockAvatarSearcher
from avatar_storage_service.mock import MockAvatarStorage

if __name__ == '__main__':
    s3_bucket_name = "avatars"
    MockAvatarSearcher.FOUND = True
    avatar_searcher = MockAvatarSearcher()
    avatar_storage = MockAvatarStorage()
    avatar_manager = AvatarManager(avatar_storage, avatar_searcher)

    # Пример вызова метода для поиска и сохранения аватара пользователя
    user_id = '12345'
    user_email = 'user@example.com'

    s3_file_path = avatar_manager.find_and_store_user_avatar(user_id, user_email)

    # Генерация временной ссылки на аватар пользователя
    temporary_link = avatar_manager.generate_temporary_link(s3_file_path)

    if temporary_link:
        print(f"Временная ссылка на аватар пользователя: {temporary_link}")
    else:
        print("Не удалось сгенерировать временную ссылку на аватар.")
