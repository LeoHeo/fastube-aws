# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Auth Model
AUTH_USER_MODEL = "users.User"

# Login
LOGIN_URL = "/login/"

SIGNUP_SUCCESS_MESSAGE = "성공적으로 회원가입이 되었습니다."
LOGIN_SUCCESS_MESSAGE = "성공적으로 로그인이 되었습니다."
LOGOUT_SUCCESS_MESSAGE = "성공적으로 로그아웃이 되었습니다."
