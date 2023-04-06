from typing import Any, Dict

from responses import GET, Response, matchers

from tests.data.service_token import BEARER_TOKEN

JSON_SECRETS_ENCRYPTED: Dict[str, Any] = {
    "secrets": [
        {
            "_id": "63ff66fae68fef382d8d4c30",
            "version": 2,
            "workspace": "6af866f8a76030530fb57a1f",
            "type": "shared",
            "tags": [
                {
                    "_id": "6401127eb9d34caabb086247",
                    "name": "tag1",
                    "slug": "tag1",
                    "user": "60cf66bab9d37ceabb05ab91",
                    "workspace": "6af866f8a76030530fb57a1f",
                    "createdAt": "2023-03-02T21:17:50.271Z",
                    "updatedAt": "2023-03-02T21:17:50.271Z",
                    "__v": 0,
                },
                {
                    "_id": "64011284a76030530f083159",
                    "name": "tag2",
                    "slug": "tag2",
                    "user": "60cf66bab9d37ceabb05ab91",
                    "workspace": "6af866f8a76030530fb57a1f",
                    "createdAt": "2023-03-02T21:17:56.816Z",
                    "updatedAt": "2023-03-02T21:17:56.816Z",
                    "__v": 0,
                },
            ],
            "environment": "dev",
            "secretKeyCiphertext": "3hezovZYz9VhcWm8",
            "secretKeyIV": "odapNBpciP0CEwhuSz67pw==",
            "secretKeyTag": "zCox5T51dcSsIRbF05fYng==",
            "secretValueCiphertext": "8TLGA67/isodKMWMfCREbQTbQ8dnyk59ufSpAJj3ZZ1ntaKhnL9Qse3f/2afgcqiYZgP6WNYeQ==",
            "secretValueIV": "w5MCP7oE082wBpZOdOxY0A==",
            "secretValueTag": "VWUNFMLdhRMlmer240ihoA==",
            "secretCommentCiphertext": "rPJ+IW3vwTjbUweDs1Z58hAePNww5tLZNZw=",
            "secretCommentIV": "hNDjXf0spbXSmq/4X3hdRQ==",
            "secretCommentTag": "wSw6EjcdhTmOojtQjf0H6A==",
            "__v": 0,
            "createdAt": "2023-03-01T14:53:46.369Z",
            "updatedAt": "2023-03-02T21:18:20.172Z",
        },
        {
            "_id": "63ff66fae68fef382d8d4c31",
            "version": 2,
            "workspace": "6af866f8a76030530fb57a1f",
            "type": "shared",
            "tags": [
                {
                    "_id": "64011284a76030530f083159",
                    "name": "tag2",
                    "slug": "tag2",
                    "user": "60cf66bab9d37ceabb05ab91",
                    "workspace": "6af866f8a76030530fb57a1f",
                    "createdAt": "2023-03-02T21:17:56.816Z",
                    "updatedAt": "2023-03-02T21:17:56.816Z",
                    "__v": 0,
                }
            ],
            "environment": "dev",
            "secretKeyCiphertext": "di+dsGILyvuva38=",
            "secretKeyIV": "Ij/+W9d/FQgneBSNaCW9Gw==",
            "secretKeyTag": "CQ5S4QCmIMY1Ra14W5yqGg==",
            "secretValueCiphertext": "bPVF6hqK5+2Jj0qzAQ==",
            "secretValueIV": "AnRDQCLInF4Mm54lEPqW8w==",
            "secretValueTag": "t36wVDlk4hxDBTA8uoaG4Q==",
            "secretCommentCiphertext": "o63sz9iKG2y6Rmajdci/aivcBbKMfyuVpV38vdMSFzT8mhVO",
            "secretCommentIV": "Uwr9ioLuiXX7Jx5dKn84IA==",
            "secretCommentTag": "ysELDOZ035EkIOP8gkqqCw==",
            "__v": 0,
            "createdAt": "2023-03-01T14:53:46.370Z",
            "updatedAt": "2023-03-02T21:18:20.172Z",
        },
        {
            "_id": "63ff66fae68fef382d8d4c32",
            "version": 1,
            "workspace": "6af866f8a76030530fb57a1f",
            "type": "shared",
            "tags": [],
            "environment": "dev",
            "secretKeyCiphertext": "Qeu0yETTFLiUgWs=",
            "secretKeyIV": "AuLVOX6URGB/zm1PljQNNg==",
            "secretKeyTag": "fWADFaBOVO6g5cGSP2eVhA==",
            "secretValueCiphertext": "DC5Awus1PksOoIGvZQ==",
            "secretValueIV": "ZyMe1bGMxHsbuMu8S4lwJg==",
            "secretValueTag": "4o6vq4qYZYGzVQvIqoIdzQ==",
            "secretCommentCiphertext": "sXhyAldsZ/7Gj5FvfvLtghgYcjLgUpE=",
            "secretCommentIV": "KuXbI0q6HhvH76tqUxHncw==",
            "secretCommentTag": "cdlpra9+aBxFk1zFLyh1aA==",
            "__v": 0,
            "createdAt": "2023-03-01T14:53:46.370Z",
            "updatedAt": "2023-03-01T14:53:46.370Z",
        },
        {
            "_id": "63ff66fae68fef382d8d4c35",
            "version": 2,
            "workspace": "6af866f8a76030530fb57a1f",
            "type": "shared",
            "tags": [
                {
                    "_id": "6401127eb9d34caabb086247",
                    "name": "tag1",
                    "slug": "tag1",
                    "user": "60cf66bab9d37ceabb05ab91",
                    "workspace": "6af866f8a76030530fb57a1f",
                    "createdAt": "2023-03-02T21:17:50.271Z",
                    "updatedAt": "2023-03-02T21:17:50.271Z",
                    "__v": 0,
                }
            ],
            "environment": "dev",
            "secretKeyCiphertext": "Mrl4Aa4LdSVL+rmfhcsfTmI=",
            "secretKeyIV": "0TLepwu7JT6Ivj/xV/TvBQ==",
            "secretKeyTag": "JvY08/VY8cX6O8tlSOE8Pg==",
            "secretValueCiphertext": "5WP2TA+aXOVfUI0f5hAkpHZxZ0Kp",
            "secretValueIV": "JZ6OG8G0dlK0rlIsGVZY5w==",
            "secretValueTag": "IFyQ67SBW4VOD2g/F9xLTQ==",
            "secretCommentCiphertext": "",
            "secretCommentIV": "IU61wN/1YubcfJOpbSYB1Q==",
            "secretCommentTag": "TuRww/GwI5k/HMk5fMTVNQ==",
            "__v": 0,
            "createdAt": "2023-03-01T14:53:46.371Z",
            "updatedAt": "2023-03-02T21:18:20.172Z",
        },
        {
            "_id": "63ff66fae68fef382d8d4c36",
            "version": 1,
            "workspace": "6af866f8a76030530fb57a1f",
            "type": "shared",
            "tags": [],
            "environment": "dev",
            "secretKeyCiphertext": "2wTbcKy5SRqeQ74=",
            "secretKeyIV": "8IQqHPDKoB+j3fcmdj4DMQ==",
            "secretKeyTag": "rs+PC9iFImURRS/Y8hwxrw==",
            "secretValueCiphertext": "YLv84AzNGsJtKQTSusq3tnZ3+iXm",
            "secretValueIV": "hBYXNno4cNgUq3pGIuzvcg==",
            "secretValueTag": "p+rnPBm8WJRZcVntzw4S0A==",
            "secretCommentCiphertext": "",
            "secretCommentIV": "uA365vf04r3KOhOQ6oAcTQ==",
            "secretCommentTag": "VpJIJ8r/stGh2jWYNShgJQ==",
            "__v": 0,
            "createdAt": "2023-03-01T14:53:46.371Z",
            "updatedAt": "2023-03-01T14:53:46.371Z",
        },
        {
            "_id": "63ff66fae68fef382d8d4c33",
            "version": 2,
            "workspace": "6af866f8a76030530fb57a1f",
            "type": "personal",
            "user": "60cf66bab9d37ceabb05ab91",
            "tags": [
                {
                    "_id": "64011284a76030530f083159",
                    "name": "tag2",
                    "slug": "tag2",
                    "user": "60cf66bab9d37ceabb05ab91",
                    "workspace": "6af866f8a76030530fb57a1f",
                    "createdAt": "2023-03-02T21:17:56.816Z",
                    "updatedAt": "2023-03-02T21:17:56.816Z",
                    "__v": 0,
                }
            ],
            "environment": "dev",
            "secretKeyCiphertext": "wBMX4Nla+OVFcZc=",
            "secretKeyIV": "vV8G9K/cPl/yOUm4J6Ux+w==",
            "secretKeyTag": "bJMiprwq2QGPHPXkVq5y4Q==",
            "secretValueCiphertext": "FHPp1vX2Pj0=",
            "secretValueIV": "PXaz6v37zPIEhccliMnA4Q==",
            "secretValueTag": "TFiZu0HrzYpqd3d1xAbrCg==",
            "secretCommentCiphertext": "",
            "secretCommentIV": "uRo+jUW0OQg+yFOHbuzdAg==",
            "secretCommentTag": "LoBAkGOi/5mzPr2dfZOAyg==",
            "__v": 0,
            "createdAt": "2023-03-01T14:53:46.370Z",
            "updatedAt": "2023-03-02T21:18:20.172Z",
        },
        {
            "_id": "63ff66fae68fef382d8d4c34",
            "version": 1,
            "workspace": "6af866f8a76030530fb57a1f",
            "type": "personal",
            "user": "60cf66bab9d37ceabb05ab91",
            "tags": [],
            "environment": "dev",
            "secretKeyCiphertext": "9cZOvFq6wUL9Rlc=",
            "secretKeyIV": "Qvy77+94ybrcordI2mWZtA==",
            "secretKeyTag": "v0Sj9SI8OTaQ8S+d+zwgdQ==",
            "secretValueCiphertext": "RLDTxFYGFsZMCh/UdlVhRg==",
            "secretValueIV": "0TLkXHKBBcuvYcGugFsTlQ==",
            "secretValueTag": "WI+P64ZVgdnOzuKK667M6w==",
            "secretCommentCiphertext": "",
            "secretCommentIV": "lCUJSY9gShpBGVpoEIjXtA==",
            "secretCommentTag": "oMC2J1YPdh6CdRV6JXSoSA==",
            "__v": 0,
            "createdAt": "2023-03-01T14:53:46.371Z",
            "updatedAt": "2023-03-01T14:53:46.371Z",
        },
    ]
}

GET_SECRETS_RESPONSE = Response(
    GET,
    "https://test.infisical.local/api/v2/secrets",
    match=[
        matchers.query_param_matcher(
            {"workspaceId": "6af866f8a76030530fb57a1f", "environment": "dev"}
        ),
        matchers.header_matcher({"Authorization": f"Bearer {BEARER_TOKEN}"}),
    ],
    json=JSON_SECRETS_ENCRYPTED,
)