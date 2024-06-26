from __future__ import annotations

from typing import Any

GENERIC_EVENT: dict[str, Any] = {
    "serviceUrl": "https://smba.trafficmanager.net/amer/",
    "channelData": {"eventType": "otherEvent"},
    "type": "conversationUpdate",
}

EXAMPLE_TEAM_MEMBER_ADDED: dict[str, Any] = {
    "recipient": {"id": "28:5710acff-f313-453f-8b75-44fff54bab14", "name": "Steve-Bot-5"},
    "from": {
        "aadObjectId": "a6de2a64-9501-4e16-9e50-74df223570a3",
        "id": "29:1Q2o9Y0pyxOhK7QU6o7DatYWMy4MFapyiHoA1r_xB2s5XsGTSxIrKOH_JGmxDXpex30trbSo3Oyh3pkXF8RnlVQ",
    },
    "conversation": {
        "id": "19:8d46058cda57449380517cc374727f2a@thread.tacv2",
        "conversationType": "channel",
        "isGroup": True,
        "tenantId": "f5ffd8cf-a1aa-4242-adad-86509faa3be5",
    },
    "timestamp": "2020-07-13T19:54:30.8044041Z",
    "channelId": "msteams",
    "membersAdded": [{"id": "28:5710acff-f313-453f-8b75-44fff54bab14"}],
    "serviceUrl": "https://smba.trafficmanager.net/amer/",
    "channelData": {
        "eventType": "teamMemberAdded",
        "tenant": {"id": "f5ffd8cf-a1aa-4242-adad-86509faa3be5"},
        "team": {
            "name": "testsentry",
            "aadGroupId": "c2d5a19b-f3a9-48ed-ade3-fc41aa861a18",
            "id": "19:8d46058cda57449380517cc374727f2a@thread.tacv2",
        },
    },
    "type": "conversationUpdate",
    "id": "f:8e005ef8-f848-156f-55b1-0a5bb3207225",
}

EXAMPLE_TEAM_MEMBER_REMOVED: dict[str, Any] = {
    "membersRemoved": [{"id": "28:5710acff-f313-453f-8b75-44fff54bab14"}],
    "type": "conversationUpdate",
    "timestamp": "2020-07-16T23:47:29.7965243Z",
    "id": "f:237e2bd0-9cd0-8aff-8469-65d891e47ce8",
    "channelId": "msteams",
    "serviceUrl": "https://smba.trafficmanager.net/amer/",
    "from": {
        "id": "29:1Q2o9Y0pyxOhK7QU6o7DatYWMy4MFapyiHoA1r_xB2s5XsGTSxIrKOH_JGmxDXpex30trbSo3Oyh3pkXF8RnlVQ",
        "aadObjectId": "a6de2a64-9501-4e16-9e50-74df223570a3",
    },
    "conversation": {
        "isGroup": True,
        "conversationType": "channel",
        "tenantId": "f5ffd8cf-a1aa-4242-adad-86509faa3be5",
        "id": "19:8d46058cda57449380517cc374727f2a@thread.tacv2",
    },
    "recipient": {"id": "28:5710acff-f313-453f-8b75-44fff54bab14", "name": "Steve-Bot-5"},
    "channelData": {
        "team": {
            "aadGroupId": "c2d5a19b-f3a9-48ed-ade3-fc41aa861a18",
            "name": "testsentry",
            "id": "19:8d46058cda57449380517cc374727f2a@thread.tacv2",
        },
        "eventType": "teamMemberRemoved",
        "tenant": {"id": "f5ffd8cf-a1aa-4242-adad-86509faa3be5"},
    },
}

EXAMPLE_PERSONAL_MEMBER_ADDED: dict[str, Any] = {
    "recipient": {"id": "28:5710acff-f313-453f-8b75-44fff54bab14", "name": "Steve-Bot-5"},
    "from": {
        "aadObjectId": "a6de2a64-9501-4e16-9e50-74df223570a3",
        "id": "29:1Q2o9Y0pyxOhK7QU6o7DatYWMy4MFapyiHoA1r_xB2s5XsGTSxIrKOH_JGmxDXpex30trbSo3Oyh3pkXF8RnlVQ",
    },
    "conversation": {
        "id": "a:1rLdrbRhx8Pc7Y6HNUmkI6QHZ4vUe1dECseFMsjCLUs61NUCtDKvf_iXhzX96AJlIFs7WgQUzTrjV3iMjbON0UfMV_gNh2tUNgHj_iY5hQoYdFu_t-hTt-uDl7m6_X4-Z",
        "conversationType": "personal",
        "tenantId": "f5ffd8cf-a1aa-4242-adad-86509faa3be5",
    },
    "timestamp": "2020-07-13T19:54:30.8044041Z",
    "channelId": "msteams",
    "membersAdded": [{"id": "28:5710acff-f313-453f-8b75-44fff54bab14"}],
    "serviceUrl": "https://smba.trafficmanager.net/amer/",
    "channelData": {"tenant": {"id": "f5ffd8cf-a1aa-4242-adad-86509faa3be5"}},
    "type": "conversationUpdate",
    "id": "f:d4414f98-25be-6cc7-b8c7-f01d51e3afd0",
}

EXAMPLE_UNLINK_COMMAND: dict[str, Any] = {
    "text": "unlink ",
    "recipient": {"id": "28:5710acff-f313-453f-8b75-44fff54bab14", "name": "Steve-Bot-5"},
    "from": {
        "aadObjectId": "a6de2a64-9501-4e16-9e50-74df223570a3",
        "id": "29:1Q2o9Y0pyxOhK7QU6o7DatYWMy4MFapyiHoA1r_xB2s5XsGTSxIrKOH_JGmxDXpex30trbSo3Oyh3pkXF8RnlVQ",
    },
    "conversation": {
        "id": "a:1rLdrbRhx8Pc7Y6HNUmkI6QHZ4vUe1dECseFMsjCLUs61NUCtDKvf_iXhzX96AJlIFs7WgQUzTrjV3iMjbON0UfMV_gNh2tUNgHj_iY5hQoYdFu_t-hTt-uDl7m6_X4-Z",
        "conversationType": "personal",
        "tenantId": "f5ffd8cf-a1aa-4242-adad-86509faa3be5",
    },
    "timestamp": "2020-07-13T19:54:30.8044041Z",
    "channelId": "msteams",
    "serviceUrl": "https://smba.trafficmanager.net/amer/",
    "channelData": {"tenant": {"id": "f5ffd8cf-a1aa-4242-adad-86509faa3be5"}},
    "type": "message",
    "id": "f:d4414f98-25be-6cc7-b8c7-f01d51e3afd0",
}


EXAMPLE_MENTIONED: dict[str, Any] = {
    "text": "<at>SentryTest</at> help\n",
    "recipient": {"id": "28:5710acff-f313-453f-8b75-44fff54bab14", "name": "Steve-Bot-5"},
    "from": {
        "aadObjectId": "a6de2a64-9501-4e16-9e50-74df223570a3",
        "id": "29:1Q2o9Y0pyxOhK7QU6o7DatYWMy4MFapyiHoA1r_xB2s5XsGTSxIrKOH_JGmxDXpex30trbSo3Oyh3pkXF8RnlVQ",
    },
    "conversation": {
        "id": "a:1rLdrbRhx8Pc7Y6HNUmkI6QHZ4vUe1dECseFMsjCLUs61NUCtDKvf_iXhzX96AJlIFs7WgQUzTrjV3iMjbON0UfMV_gNh2tUNgHj_iY5hQoYdFu_t-hTt-uDl7m6_X4-Z",
        "conversationType": "channel",
        "isGroup": True,
        "tenantId": "f5ffd8cf-a1aa-4242-adad-86509faa3be5",
    },
    "timestamp": "2020-07-13T19:54:30.8044041Z",
    "channelId": "msteams",
    "serviceUrl": "https://smba.trafficmanager.net/amer/",
    "channelData": {
        "tenant": {"id": "f5ffd8cf-a1aa-4242-adad-86509faa3be5"},
        "team": {"id": "19:8d46058cda57449380517cc374727f2a@thread.tacv2"},
    },
    "entities": [
        {
            "mentioned": {"id": "28:5710acff-f313-453f-8b75-44fff54bab14", "name": "Steve-Bot-5"},
            "text": "<at>Steve-Bot-5</at>",
            "type": "mention",
        },
        {"locale": "en-US", "country": "US", "platform": "Web", "type": "clientInfo"},
    ],
    "type": "message",
    "id": "1598889368164",
}


DECODED_TOKEN = {
    "iss": "https://api.botframework.com",
    "serviceurl": "https://smba.trafficmanager.net/amer/",
    "nbf": 1594836399,
    "exp": 1594839999,
    "aud": "msteams-client-id",
}


DECODED_TOKEN = {
    "iss": "https://api.botframework.com",
    "serviceurl": "https://smba.trafficmanager.net/amer/",
    "nbf": 1594836399,
    "exp": 1594839999,
    "aud": "msteams-client-id",
}

OPEN_ID_CONFIG: dict[str, Any] = {
    "issuer": "https://api.botframework.com",
    "authorization_endpoint": "https://invalid.botframework.com",
    "jwks_uri": "https://login.botframework.com/v1/.well-known/keys",
    "id_token_signing_alg_values_supported": ["RS256"],
    "token_endpoint_auth_methods_supported": ["private_key_jwt"],
}

WELL_KNOWN_KEYS = {
    "keys": [
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "JW3EXdnw-wY2EqLrWTqQ2rUkB-g",
            "x5t": "JW3EXdnw-wY2EqLrWTqQ2rUkB-g",
            "n": "q9yUmEOTvAl-GXixICld8oMr1f4-qAS8T7FncPRMjrNylGPZ0-efaxIQ1p8lU0K0hs_i4G1hnLppmLj8RJPXotioB5ffCacBZqiMLe2RQTdpcoGsZVImaF1FHnAQwdCD6OFaLO-GmcEg84tK7uwXHPp_JEBbtDS9J6k91ornQ3EwDyfMFocNaZl3dG_6plXLRf05Fm2LaR70-KN18OfJm7lwNeci67RJu1pPKJ2ep_DXG6MaMcapvoCYDESOn23l606pS-icydOx5R5B26jqFewo_aUorT__r5XSti-GbwXL5LWGXqGiDaxCv9Kf1IfZQD8hYRuS3UaAAALWmPqPDw",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": [
                "alexa",
                "directline",
                "email",
                "facebook",
                "groupme",
                "kik",
                "skype",
                "slack",
                "sms",
                "telegram",
                "webchat",
                "line",
                "test",
            ],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "yAVt9Pqi6ErxveBKNVwsmDgVC0k",
            "x5t": "yAVt9Pqi6ErxveBKNVwsmDgVC0k",
            "n": "y9XhbyVRwuVN0JGdkgHEujsd5-sKRlPj2-MraqQ2QSgOupvI97cWcycMxV7rLd_8OURq-uJ5Kq8M57S0yDc-14sY4Pk4rl0MBQqEJ_b99us4EHUBurkYo-xDPB25Ey11phhWAKk0r-1bECcbDFsgJQP5tmwjRADdPR1d7JeCfU6_GnI8FxkzQZ-7kKh0rQkhNXnR6ZFuNOlpr5OD7uQog3voFEMAkkyEO7lPDzp0aayqYiC4Gxzt0eROY3i-7lRjTtwNmN3A57k2pYhb0qS1TkrD4QFe_TCn76irIrGUOrthlQDtTQQimYhV9mCJEp7L-9u22sdS0LnjU3k7OvITYw",
            "e": "AQAB",
            "x5c": [
                "MIIISDCCBjCgAwIBAgITHAAY55wmi82KxRZEFQAAABjnnDANBgkqhkiG9w0BAQsFADCBizELMAkGA1UEBhMCVVMxEzARBgNVBAgTCldhc2hpbmd0b24xEDAOBgNVBAcTB1JlZG1vbmQxHjAcBgNVBAoTFU1pY3Jvc29mdCBDb3Jwb3JhdGlvbjEVMBMGA1UECxMMTWljcm9zb2Z0IElUMR4wHAYDVQQDExVNaWNyb3NvZnQgSVQgVExTIENBIDIwHhcNMjAwNDI4MjIxNDUxWhcNMjEwNDI4MjIxNDUxWjAlMSMwIQYDVQQDExpqd3Qucm9sZXMuYm90ZnJhbWV3b3JrLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMvV4W8lUcLlTdCRnZIBxLo7HefrCkZT49vjK2qkNkEoDrqbyPe3FnMnDMVe6y3f/DlEavrieSqvDOe0tMg3PteLGOD5OK5dDAUKhCf2/fbrOBB1Abq5GKPsQzwduRMtdaYYVgCpNK/tWxAnGwxbICUD+bZsI0QA3T0dXeyXgn1OvxpyPBcZM0Gfu5CodK0JITV50emRbjTpaa+Tg+7kKIN76BRDAJJMhDu5Tw86dGmsqmIguBsc7dHkTmN4vu5UY07cDZjdwOe5NqWIW9KktU5Kw+EBXv0wp++oqyKxlDq7YZUA7U0EIpmIVfZgiRKey/vbttrHUtC541N5OzryE2MCAwEAAaOCBAgwggQEMIIBfgYKKwYBBAHWeQIEAgSCAW4EggFqAWgAdwD2XJQv0XcwIhRUGAgwlFaO400TGTO/3wwvIAvMTvFk4wAAAXHC5KCDAAAEAwBIMEYCIQDeN+vxXw41cyBnN4dq9+AoeuvSghmYdR9TZaHi0zFUEwIhANRXxq8L53r6dQ8MzNT9Ioj93f3kj608SDyLp60LVDvEAHYARJRlLrDuzq/EQAfYqP4owNrmgr7YyzG1P9MzlrW2gagAAAFxwuSgjQAABAMARzBFAiAuoOdAikClHRaxXtaLyZQRnNeUcEWzAFrSqjwdQ90y/QIhAJj9+WFX3bbupyb+rKx8yemUCL4PKcGBxMhvOz8qpZN8AHUAVYHUwhaQNgFK6gubVzxT8MDkOHhwJQgXL6OqHQcT0wwAAAFxwuShsAAABAMARjBEAiBFF5QGF0rOiN+WieRGVn4FmicQerGiCYFQtqbbhtJXYgIgPasRkRuFE2xa+aM3LgLFmfLmmMmbAU2hjyw47GZvSGQwJwYJKwYBBAGCNxUKBBowGDAKBggrBgEFBQcDAjAKBggrBgEFBQcDATA+BgkrBgEEAYI3FQcEMTAvBicrBgEEAYI3FQiH2oZ1g+7ZAYLJhRuBtZ5hhfTrYIFdhNLfQoLnk3oCAWQCAR0wgYUGCCsGAQUFBwEBBHkwdzBRBggrBgEFBQcwAoZFaHR0cDovL3d3dy5taWNyb3NvZnQuY29tL3BraS9tc2NvcnAvTWljcm9zb2Z0JTIwSVQlMjBUTFMlMjBDQSUyMDIuY3J0MCIGCCsGAQUFBzABhhZodHRwOi8vb2NzcC5tc29jc3AuY29tMB0GA1UdDgQWBBTEcU79W2A5rki6OUBtgHRulPd+SDALBgNVHQ8EBAMCBLAwJQYDVR0RBB4wHIIaand0LnJvbGVzLmJvdGZyYW1ld29yay5jb20wgawGA1UdHwSBpDCBoTCBnqCBm6CBmIZLaHR0cDovL21zY3JsLm1pY3Jvc29mdC5jb20vcGtpL21zY29ycC9jcmwvTWljcm9zb2Z0JTIwSVQlMjBUTFMlMjBDQSUyMDIuY3JshklodHRwOi8vY3JsLm1pY3Jvc29mdC5jb20vcGtpL21zY29ycC9jcmwvTWljcm9zb2Z0JTIwSVQlMjBUTFMlMjBDQSUyMDIuY3JsME0GA1UdIARGMEQwQgYJKwYBBAGCNyoBMDUwMwYIKwYBBQUHAgEWJ2h0dHA6Ly93d3cubWljcm9zb2Z0LmNvbS9wa2kvbXNjb3JwL2NwczAfBgNVHSMEGDAWgBSRnjtEbD1XnEJ3KjTXT9HMSpcs2jAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYBBQUHAwEwDQYJKoZIhvcNAQELBQADggIBAIFDzL63y9zdfNBXHs+miigmo5uCloVOIKe00s6MSAkQ5C+cCbqlTPwdXzD1eESgacPfNBjbERseVQsvmu696j9q5RYoa8NZynlPL6FNaxsR3+PaI2DIMvkhId6amUXFp7unZKlfzP6WTjnFhg/rKilwKW12jooB3HYmFaKQg8zawFkdz4SZ3lSnvTv8AmkBv6T7ea2FiKzmmoX1BLk9C8VNR0SwQXrxKXYv2cYLnFhfUI5eO4cLoAJS3ID9IAaeePvfKkTQv3v32t2gaiYYQarpShz8k9qYxf1apQ9r2ax48hFlAE/u+TpdtgpjUfFurhOfQSZiitMdueYBPImQADMqX8eZNouH8yaaOkc1j4xZJG7eIwp0ZD1zxMziZlxdFbsNXH5Js3fSE5Yntqh2Jm+MjeJqmnNCh1Fh7tj1VhdBCs4RnS2MCO/oTOp7w8ioQS4UK9iJXwHn2BhbGxg9riVfErEghGQB5RGPi5pQFSwr9XR2D5aJmap5xx5KQ3yfGGhtaS+SCTGMkTwZQq4K6ETKxV2MWYgbgXDDjmA2RYV6L1fWlf81ERPiiv16MBx4vevBZPGFDGZlmZc9XiZCJSMYr2Ryl7O24t8UBV6iul3UQpsdlRmK+bvNtCjfDfwuSh+9s1qTJ/btginq3eg0crJTuCZd0E3Wr+OP4prmvdZF"
            ],
            "endorsements": [
                "alexa",
                "directline",
                "email",
                "facebook",
                "groupme",
                "kik",
                "skype",
                "slack",
                "sms",
                "telegram",
                "webchat",
                "line",
                "test",
            ],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "j8J0edkw932giTt55vv7Ylqdn7g",
            "x5t": "j8J0edkw932giTt55vv7Ylqdn7g",
            "n": "4VdinJLdWh-WcqM8vimR3drKtpc0yj_QaY24SZrBszwSe2QyNTVKRKiarldHZ9DjV7Mr_cdUX_3Z8_CNn4jz7oLFy34hXTqAvqwUOg5H-6qbZBkscbbfl_1Wj-frl3Cw4NxixUZWzUrNStmI38IvFAAL24sLDT5EUNmhB5J84xhEgxNPquhwkq6IitiC2j_CRafzr11KVZOnSDFam0rQmS7OET0j0N1nFtZxNGl62yek5xiwIOoUCVQYCQGMcWtbs1ErLc3kmOOrWFxzRdzmZU1xmgU_YzrOLbBckrfUrWk4bX29Id2i5yRvP1hxNm1bvLufM9MGO8WYwRDdlVml6Q",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": ["skype", "msteams"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "0FnYjMoKrnRZg9hlC7EwTd3doXU",
            "x5t": "0FnYjMoKrnRZg9hlC7EwTd3doXU",
            "n": "xzt1UNT6lgYfWboy64y2HiWfseqtgbBRoLbuVxKU6g8u3UtpbGXkgRKd-0AeuNOPfwrFz30DaRdEw4drCDhVxleKQyix7s6hWF2aHYAiFm-PffrfJCqEUsjzKyzTP4qu6NY3RC685noe6EDEZ7coxy41dmHliYiSStCOjZWHY8trSayCxQbRdkrTWrXu1BYY6da6RUvrdatWOjQM6gFYrXNczkbw4PnN7WqtQvR7p3gStT-3JKL5VIjGed_r1TuSSvm6woqTLIMwEnY-BG4cWHaGERMOPXNUltkeW9kLtO9kynB0gl05K7vPONMo9By9KlHJ44oOY5HWOlsQD_cgww",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": ["cortana", "o365compliant", "nightwatch"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "xfcct4RNFp_ZA7xlHEzOBfpm8UI",
            "x5t": "xfcct4RNFp_ZA7xlHEzOBfpm8UI",
            "n": "nBqW3H-V5oB3owEf8ENFcLlWeynByrYLkC4Rj7izUZQVPqpsJdVrRLNVPMSHwAUrmqAwIulSGuyeA49wHUOK-0DOHaPzLyV1l9DlW4uOBqonwlocO9Hu-WnGz84khJF5xf1eknxkVZ_SpieBibBvhIuCdILKOVxSUEdeirh_HNVg5JB1VlrDNl1oKjRyHQ8MggY6jGd5K1oUxh2Ffgkkn1pGE2HNG4dkSwn7XnMY7ir77ZJo8KWAWiAS9IgeMnxBGXq7xQLLbiZY14IAGs3Xp7m5yDpeH8fr6QAN3Uba-5F4pZ41Mz894zNXMaKlTwk7__E6HL98dX2kv0xbZMewMQ",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": ["cortana", "nightwatch"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "mzY3m-NE-4882sRuP5h78aTyONA",
            "x5t": "mzY3m-NE-4882sRuP5h78aTyONA",
            "n": "t1WmS--bXlb9VNZ23IyVn0DpKfBzY4_d2Z03vhZp1FSRHZp_9R-8DtDwSEEpD6jrsHzgTnKUllL9M3_G_pbbWHXdjig01iiv4PDnzx7-2QOUSY6YV5g4xMxE4uxfPJvyRyII1ZqKHxubdagZkv744gXYGKJwwi2FmLHTFwmk4wesL1-W-AEbSeaPxNdTbLkWqNL80jAGCZZWkTozWPrUrjQW1QQkaFf_y7Z5JsD5Lb-cVx-I_TfIZOitaIyLnud8voY7c2W1mY0-3awdTouQCnlt6EGTSjYEfPRIyCPPu7NAq3MDzoNiMto6x0T__oSe4nz61jPYvLvtTOSPqaoCAQ",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": ["cortana", "o365compliant"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "5KMhAVP3bOnUdnY-cyl_WTxRvSI",
            "x5t": "5KMhAVP3bOnUdnY-cyl_WTxRvSI",
            "n": "p2DRx4RpaPA2OD9u2fI7EeIx_pYavl_bGNONQpnBlkQy2jR9GGGAa2BpkKWdlmXxym-qCIgX1QWYMZ_KCyTd0IWqlZ3vpGtQnlaxdPAyw9WHy35C2CeCsX8Y78hbfnm9itPTA6mxZj7UkYzTtmG9dtK-A0vfq_P2wpjuEzvgi8QVd5GGM8qtEEjsGQ5oWo2cHWMuIXZVTxroYCZPygSiTQdyUWr_WuMo0tDJlH-kYSFM3srAWVOWnXwj4XOP5z-D9tc9yoJvKWc5Xiq5iJ8qMfix2JEb8Y1gn1cOfGbSMf91E1mElT3nP6nNesHjnaEWC-OVY31MM1J0IRFRGErqIQ",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": ["cortana"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "TdFMxqe-ZsRttgpmIW1kM8QRnWk",
            "x5t": "TdFMxqe-ZsRttgpmIW1kM8QRnWk",
            "n": "rLSQjpoiXzuLPiFdVuIzaNQrTEC2OdkzqQL8ST96rlCJpqUQ_XG5iKv0MWhiKIGunem5Z-p59G_MsnptVAw9AA9FobmYQcBadskDpiqiZIBWloa0cN-qQnVw-RcdoWu-iElahlmgaan_R-HddXEXnuL19tVRDGpkzslUCSj4EtH2Nzq-pQXX0i6g4V3IOl7j9oDbiznr6YXuYSWbo2z4CSrvnGL8vtVWlF1O2FsPYWxQ137e7r1bEIYiC_jLqB-hLJQWoUyg8jMwnImGIVAxQvt212ZrpT2hnH9mH0FI76O0SwS3I4OlzMZCGSXf8mrbOGgzybqa35NSsnL_DCne8Q",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": ["directlinespeech", "telephony"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "mnG8cY8kjzYQGSAQrZOMspTlTE4",
            "x5t": "mnG8cY8kjzYQGSAQrZOMspTlTE4",
            "n": "yoaKaiAGa97tvYxAVan2rzv3MeuyGR3Y0z5DyrpF5bbAmF8xRB1aNBZK0XXUI25muJxyaQTtaMl5U3vNQKrSpfHizJN-ZIaxbCkrvsv_ay7SCNVeYLomKB5J7IPtHxFexgzKuaiMyBQTr6w728DIIf5L6MiN7iE3bTXMPHOXDy2-ZndnM5-a4OZXJTl_580KLY93oeJyaeNL-7s79J90ITwmd7qxGOokZ_NUXGQzRWmCkRztMrtexLEob5_fP0UE04diiKpbK1v3h67s-lto4tMKyCFYvOxqOQAAm1mNyGvG1TLGGjjMY2m9HqnVXVcGYfbCltyf8syGFM6NMzOG_Q",
            "e": "AQAB",
            "x5c": [
                "MIIHGjCCBgKgAwIBAgITOgAeyciCCL/AdEoDxwACAB7JyDANBgkqhkiG9w0BAQsFADBEMRMwEQYKCZImiZPyLGQBGRYDR0JMMRMwEQYKCZImiZPyLGQBGRYDQU1FMRgwFgYDVQQDEw9BTUUgSU5GUkEgQ0EgMDEwHhcNMjAwNjIyMjExODE2WhcNMjEwNjE3MjExODE2WjAxMS8wLQYDVQQDDCYqLmNvbnZhaS1mcm9udGVuZC5zcGVlY2gubWljcm9zb2Z0LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMqGimogBmve7b2MQFWp9q879zHrshkd2NM+Q8q6ReW2wJhfMUQdWjQWStF11CNuZriccmkE7WjJeVN7zUCq0qXx4syTfmSGsWwpK77L/2su0gjVXmC6JigeSeyD7R8RXsYMyrmojMgUE6+sO9vAyCH+S+jIje4hN201zDxzlw8tvmZ3ZzOfmuDmVyU5f+fNCi2Pd6HicmnjS/u7O/SfdCE8Jne6sRjqJGfzVFxkM0VpgpEc7TK7XsSxKG+f3z9FBNOHYoiqWytb94eu7PpbaOLTCsghWLzsajkAAJtZjchrxtUyxho4zGNpvR6p1V1XBmH2wpbcn/LMhhTOjTMzhv0CAwEAAaOCBBYwggQSMCcGCSsGAQQBgjcVCgQaMBgwCgYIKwYBBQUHAwEwCgYIKwYBBQUHAwIwPQYJKwYBBAGCNxUHBDAwLgYmKwYBBAGCNxUIhpDjDYTVtHiE8Ys+hZvdFs6dEoFggvX2K4Py0SACAWQCAQkwggHaBggrBgEFBQcBAQSCAcwwggHIMGYGCCsGAQUFBzAChlpodHRwOi8vY3JsLm1pY3Jvc29mdC5jb20vcGtpaW5mcmEvQ2VydHMvQlkyUEtJSU5UQ0EwMS5BTUUuR0JMX0FNRSUyMElORlJBJTIwQ0ElMjAwMSgyKS5jcnQwVgYIKwYBBQUHMAKGSmh0dHA6Ly9jcmwxLmFtZS5nYmwvYWlhL0JZMlBLSUlOVENBMDEuQU1FLkdCTF9BTUUlMjBJTkZSQSUyMENBJTIwMDEoMikuY3J0MFYGCCsGAQUFBzAChkpodHRwOi8vY3JsMi5hbWUuZ2JsL2FpYS9CWTJQS0lJTlRDQTAxLkFNRS5HQkxfQU1FJTIwSU5GUkElMjBDQSUyMDAxKDIpLmNydDBWBggrBgEFBQcwAoZKaHR0cDovL2NybDMuYW1lLmdibC9haWEvQlkyUEtJSU5UQ0EwMS5BTUUuR0JMX0FNRSUyMElORlJBJTIwQ0ElMjAwMSgyKS5jcnQwVgYIKwYBBQUHMAKGSmh0dHA6Ly9jcmw0LmFtZS5nYmwvYWlhL0JZMlBLSUlOVENBMDEuQU1FLkdCTF9BTUUlMjBJTkZSQSUyMENBJTIwMDEoMikuY3J0MB0GA1UdDgQWBBRADS4OB9QzdbNP8PFiTwoP/R7m8DAOBgNVHQ8BAf8EBAMCBaAwMQYDVR0RBCowKIImKi5jb252YWktZnJvbnRlbmQuc3BlZWNoLm1pY3Jvc29mdC5jb20wggEmBgNVHR8EggEdMIIBGTCCARWgggERoIIBDYY/aHR0cDovL2NybC5taWNyb3NvZnQuY29tL3BraWluZnJhL0NSTC9BTUUlMjBJTkZSQSUyMENBJTIwMDEuY3JshjFodHRwOi8vY3JsMS5hbWUuZ2JsL2NybC9BTUUlMjBJTkZSQSUyMENBJTIwMDEuY3JshjFodHRwOi8vY3JsMi5hbWUuZ2JsL2NybC9BTUUlMjBJTkZSQSUyMENBJTIwMDEuY3JshjFodHRwOi8vY3JsMy5hbWUuZ2JsL2NybC9BTUUlMjBJTkZSQSUyMENBJTIwMDEuY3JshjFodHRwOi8vY3JsNC5hbWUuZ2JsL2NybC9BTUUlMjBJTkZSQSUyMENBJTIwMDEuY3JsMB8GA1UdIwQYMBaAFNIc0vGNgMZLVTgdso6Elvs8IH7JMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjANBgkqhkiG9w0BAQsFAAOCAQEAdfSH2OObE8HNHSV2pyCUOnLTl45I5zD3Thi1fWMr+C9yXNeAtMdMErmm4UJsAQlJU+JD+36FenB7XGUBIqh+priZNNYgt7Zi58TsSC9kV92vcdbxodDbicCOw/Z6ospNrn/rvL+SHguJv9W/7zV0ySiXyySjBIISsrzCfIx2FK25ByJNcqSopUyI8LGVDI0dalJtXtnl8KpBbFXl7KqZU2gL1imotDfx56PhOZCuRQNTx0jkBxNTE3Rp4cGo1v3pvwCpkB/ynuQSGyPn32BPP/wkdcKQOTA/ZmLmMWJdLUdheORGPc741n1cq+itmOavhmVgJXzdC8kAZgk65hbkfA=="
            ],
            "endorsements": ["directlinespeech", "telephony"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "IGNygSWnukDiRnhxhmfwHot8Ras",
            "x5t": "IGNygSWnukDiRnhxhmfwHot8Ras",
            "n": "zmNPwHqs7Cak7oEV7cBezHocJPRLL1iWO4RnabHj0nKmEhnRoG5Z-L1fBW5v5x0fAnu5nEJ44EGYTq2SJnKjKWWloAyCdiHv6dwmArGRWDOMICFMfebLVdttRhnP7eLSJxXRWqyCHPKzwvHl1WHtCjTaJVmpRJAM_XKMjqG2mxzNZdnGrJKhp3Y2TtQHSvPw62kYIHlR84Yv00XztNGutAZuJWdCyKAPBqYPWj-Ipog-h0NWFU9zsMfAoh_ZQRg3nzD_3SW0Kg-FDAFqL7BYR71iJQ7_hmLBNqTD4gDGW9sAXvZtuFbpEItnW9EwAeQD1X_w4eLuEsZAjyVXfwNqLQ",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": ["skypeforbusiness"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "Su-pdZys9LJGhDVgah3UjfPouuc",
            "x5t": "Su-pdZys9LJGhDVgah3UjfPouuc",
            "n": "twNA0icsYL3PBUjLMpWsSF4rhQWErURCWyeAnosGYwWnI2JhmzKnlY-tpq5fYi9-yNMrf5WMVp1vAszaVIq-yQbZSRfxbYJSiVQsTDk3ycYcdeqYfqELGPOH7bwgeEe4uG5mi8NzGCXXdl6eu70cIgLHEfrC3UI2gpYUSjrcvvx3OoE5N5xi3-In27X6YMrRjKkrTAcPLiesz_FRTaw65YBXNpsZnWpXHjs9zNnjRSCQeHIWnOLpzzRmsPaMgVe6pBT7GnsEn-aB-K6StiyXlZlEvsjU5k2X2ZpH2rCO_Hyp1DqgMIYWyP2dUcidTP2IK8_koahDl3Gp8luqzEN2QQ",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": ["skype", "msteams"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "Uw1mDDTaIDZppF0fdzDsZNqquk4",
            "x5t": "Uw1mDDTaIDZppF0fdzDsZNqquk4",
            "n": "p9sOW0r8N7yXU7oj-cXfkkpvbmuWAa-6eatxK_L-sqLp4mc75j7SUgeCuoz_GFGzSaZN2PfCGez5_22unAFSDQz1orUHX07idpyUAn0-GUk8pRq0jaPN3XgbOfZ8bY1Ny5Td8T_Sh6BEB3hfis0kMX_erHZA1tLHsG1FQ-rsu9NJ3fw9O2LEFHqmFZo_KR5bWIuFdk-3LSTZrM74N_kJ9lqvAmrAsHUrOW_uuXmF_nT3CqtTpyfiUJn8eWlgW97TL6gLViM4NCK655QJ7KVIwmSyIsqMc_De-bOll5FB-3alzyBNfafh_eycMSmQdCk4CShYaz3y8C1p0zKxpiNsDQ",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": ["msteams"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "vjzFLJiFl6CybpKaPXMJmIKSlWw",
            "x5t": "vjzFLJiFl6CybpKaPXMJmIKSlWw",
            "n": "r-bam9J4QLgqYnxgE9EawufQzvloHPX758Rp_A5ESwA7Av3fWPusx95adD5jDHPCYud5YErOiaqqAkiqDjUxGVzZa5f4kv1xc-iBAJFzv2r5AYDHrXBq1tA6xEGjvaHW8hkzHQUP_2WgSVHzkGbLVOwz46UwXRySsZaxY5VE8iFLQTmr1Q6zwFNbAFxoZ_q0WcP_VkfwBncPb7RW4pzZPp_lXIY_b64JfyUG39QCVSPna9DhAKdHH_Ms5L7qhPLb2eb0acrVV4q9VIp6bBZUqOa5qICKMi6RzvQ3h-EyGzz1m8nYFwgrSMXN-5OBTX_WNv9wVB0YGbeQlJO7AK0KDQ",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": ["skype", "msteams"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "X66SlOZOTSJpfEyzQyREQQvzfvE",
            "x5t": "X66SlOZOTSJpfEyzQyREQQvzfvE",
            "n": "r_lMrPefUSg7hZAA9maQ4-rSb6nAjyO1bs3xCHqoq_RmuYSG6yYiIP4KrdO0mPxXV-CHvzxagFqBvx_BZjERLg5kxj-Dwc0h28dudTm6r7k1HKdqKi3GxQFpwhX4lo7UvYcaSEi1RvIQtrpTUF4cd412QrzRUHsikeqtzUhtOqWEQ4y6FKk9AtXHCygfHSo4FH8LRFcXYUcSBS8wBkb-Ws62vz-DqCgxkgVJk5FxX_auGJvvGfQgMjrQ6cur2Rw9ZIV4uowgKPQlud9IFMLG7qCrpsTR9oObpWHbvCsLuC8hCDKNI6uqxIM4tsw9ISLNRTO0jXYufuElygF-0XI__w",
            "e": "AQAB",
            "x5c": [
                "MIIFEzCCA/ugAwIBAgITVgBYYXuIN7aLYOOFOwAAAFhhezANBgkqhkiG9w0BAQsFADAVMRMwEQYDVQQDEwpNU0lUIENBIFoyMB4XDTE4MDQxOTIzMjAxM1oXDTIwMDQwODIzMjAxM1owKjEoMCYGA1UEAxMfY2hhdHNlcnZpY2UtcHJvZC1nY2Mtand0c2lnbmluZzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK/5TKz3n1EoO4WQAPZmkOPq0m+pwI8jtW7N8Qh6qKv0ZrmEhusmIiD+Cq3TtJj8V1fgh788WoBagb8fwWYxES4OZMY/g8HNIdvHbnU5uq+5NRynaiotxsUBacIV+JaO1L2HGkhItUbyELa6U1BeHHeNdkK80VB7IpHqrc1IbTqlhEOMuhSpPQLVxwsoHx0qOBR/C0RXF2FHEgUvMAZG/lrOtr8/g6goMZIFSZORcV/2rhib7xn0IDI60OnLq9kcPWSFeLqMICj0JbnfSBTCxu6gq6bE0faDm6Vh27wrC7gvIQgyjSOrqsSDOLbMPSEizUUztI12Ln7hJcoBftFyP/8CAwEAAaOCAkUwggJBMCcGCSsGAQQBgjcVCgQaMBgwCgYIKwYBBQUHAwEwCgYIKwYBBQUHAwIwPgYJKwYBBAGCNxUHBDEwLwYnKwYBBAGCNxUIh9qGdYPu2QGCyYUbgbWeYYX062CBXYXe6WuB1IVnAgFkAgEUMIGFBggrBgEFBQcBAQR5MHcwMQYIKwYBBQUHMAKGJWh0dHA6Ly9jb3JwcGtpL2FpYS9NU0lUJTIwQ0ElMjBaMi5jcnQwQgYIKwYBBQUHMAKGNmh0dHA6Ly93d3cubWljcm9zb2Z0LmNvbS9wa2kvbXNjb3JwL01TSVQlMjBDQSUyMFoyLmNydDAdBgNVHQ4EFgQUVgxRS2z4ctcXATfMYQ3newWIIWYwCwYDVR0PBAQDAgWgMCoGA1UdEQQjMCGCH2NoYXRzZXJ2aWNlLXByb2QtZ2NjLWp3dHNpZ25pbmcwgbUGA1UdHwSBrTCBqjCBp6CBpKCBoYYlaHR0cDovL2NvcnBwa2kvY3JsL01TSVQlMjBDQSUyMFoyLmNybIY8aHR0cDovL21zY3JsLm1pY3Jvc29mdC5jb20vcGtpL21zY29ycC9jcmwvTVNJVCUyMENBJTIwWjIuY3JshjpodHRwOi8vY3JsLm1pY3Jvc29mdC5jb20vcGtpL21zY29ycC9jcmwvTVNJVCUyMENBJTIwWjIuY3JsMB8GA1UdIwQYMBaAFGHLu4ZhQWMy1Vtmxo63nE0AbwT5MB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjANBgkqhkiG9w0BAQsFAAOCAQEAkaZ/sGrblJCCJn4rzUGXzHuyC4KY/iZu65hrLjcDTR0O09Wl87KfYCSP50yVRtSj3mHdL/Yph6h8qYVhlCgoGjsykS3WPivn7CTc8sGFDapqZUav/QMEK/zKjq4TOJzB+0Q058GGGaNRoMBG+Qm48ZtSGp5TgX67dxi94A11O/qDnZywO2fq/+pfToDezo2kOlXU/JDbCwXqJ11OsuSQPXWXLG/QtKMNtkx3lvOoRtSbN8i+XytVae7kGJnx/G0aCD6RygxZUy4FxT38CKYHDuGe3CWbUoPUUHpDONq9yO0O3v98AQZg5UwriWQaZQxoRBYhocCc1RErl89G6+qXEQ=="
            ],
            "endorsements": ["msteams"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "AfPKMgt9TFhQaxJLxxOGOe4-3Dw",
            "x5t": "AfPKMgt9TFhQaxJLxxOGOe4-3Dw",
            "n": "4w48eBk_3mk_B79Yrqu_e8xgWvxGpXstaqmZr24M0MkKOwoEk53qY9NwNB0NUIPKhZuz56ncX969MHrurCkY7pyc4M_nwlqyguyG1svxnjtH4TtwoWj1CzJ7hfPu90OIrwYye7Nd4jea1_ZSoGwXM4GAHvJR7pvdotcahtkpg84qvWJ5SBoCE21sb9KgB0_Zx2qxZaC8YG8sa4HLsl_u4KjMntfg-yYyORaKQ-N4XPCBT_u4kocr_BnvaWr8VOMx-OJdUNWOTjHGaevF00bHvPfUCRya8_iApgs1LqraLppzfambE1bq7kUOSvtIG3bu2vqkoUtWoadWJzCQRwkpVQ",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": ["msteams"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "eI9vuIlZxhDfrIgBqdJQ5ch2dCY",
            "x5t": "eI9vuIlZxhDfrIgBqdJQ5ch2dCY",
            "n": "swV63iUx7ZaKJ5xXKQUc47UtPMTBt8PewGU-OIlg9Krf87cx_Ph86_wdcHT1xTNKK1RXwIWDN40EBnvg0My8kxfdKmJv8rNETy7OQXg2UeE5oCYJvl5dayqhMGe416Y-rKkPNRFvF6fhPZKZ1RUiOJoUcym7bxh3zlbKGRC752zVstyVU6mc2VQJh-YUaIhfLWImmPozjYJAiTEd_KvCPgb74NjxVJX9lz-GvbXrqfrItWHUcm8YYa9CdevCtXu15MnLT4BIPHkLNwXrDMN7OYdm-bP7Wy_1rW2qk0xXWpt7skSQ8vCm7T_milaQjD9Bi-I28CVulgbpusMvCew_hQ",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": ["skype", "msteams"],
        },
        {
            "kty": "RSA",
            "use": "sig",
            "kid": "oULffynML1NPtz1r0jm6NcavN9U",
            "x5t": "oULffynML1NPtz1r0jm6NcavN9U",
            "n": "2ZhvikV9Kgicu-TpKfT_Yr1VVbxF4SaiqbVvJ0xDv5KoYR3qlktVkxLP7EhqiS8bLs8GEr0HuDHVXGjl5o73sAksAlanKH_F1ypTKEJG9L9sVLqui9di65JhLumaprYgQsW2lMAQf_7JeU9J3BTsb09SVxTmbCefIuRatqxGYaQvvI7I7O9woglWwFFWDOV5zXa9HBeE13rZAMVVPHcjLWP5SEwNCIeYlU7dItWBq9n7ukwZTV8_bH7BrYEVA59a1iaQoQWVbWRXWkJEoM-FrhBkD5ihS1nriaK5PM9GUMr7xU-YMgpyyN4t07R2h0hNMqJORrMVPPbCPPZsjLn3wQ",
            "e": "AQAB",
            "x5c": [
                "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"
            ],
            "endorsements": ["kaizala"],
        },
    ]
}


TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlN1LXBkWnlzOUxKR2hEVmdhaDNVamZQb3V1YyIsInR5cCI6IkpXVCIsIng1dCI6IlN1LXBkWnlzOUxKR2hEVmdhaDNVamZQb3V1YyJ9.eyJzZXJ2aWNldXJsIjoiaHR0cHM6Ly9zbWJhLnRyYWZmaWNtYW5hZ2VyLm5ldC9hbWVyLyIsIm5iZiI6MTU5NDkyMTkxMCwiZXhwIjoxNTk0OTI1NTEwLCJpc3MiOiJodHRwczovL2FwaS5ib3RmcmFtZXdvcmsuY29tIiwiYXVkIjoiNTcxMGFjZmYtZjMxMy00NTNmLThiNzUtNDRmZmY1NGJhYjE0In0.PlgPPzOUGR89dgyEmOHil159YRrdhxK9CTx9PJeilhX1mawcC6p1LVPd3nweRtkw72vb9XFtjTVqw2oJBtt2XwP-lXwb5p6DWR0wsedduZ1dLMpXj8E14SwNIq8tg1xLIWgWYUZSmA4Sr9lnpKKOI8i2lrjo6BAkFC_RQK9QYkyt-HJsIOmEdg4_9uBwWvVrlyvssX4kVwyEtsRZLu0S-QjbZhL7DXA8AA7P-5dfmdzxUt7SGO6yC5hceado_pgS9M3JRkL3H5DQdxm0q0kPYn4i_OJHYqQ73EMJ9StYkmKpuu4DgvRTSo7TPaIqMkcM0rLWkdOrEF2t8I0-g9J9Tg"
