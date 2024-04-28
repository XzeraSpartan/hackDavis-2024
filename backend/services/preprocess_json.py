import json
null = None
# Sample JSON data from your API
api_response = {
  "status": "success",
  "quota_remaining": -1,
  "text_score": {
    "text": "\u201cYes.\u201dsaid Canine \u201cI know exactly what\u2019s wrong, The children are beginning to eat far too many sweets and are not looking after their teeth at all.\u201d \u201cI know\u2026we can fix it!\u201d",
    "word_score_list": [
      {
        "word": "Yes",
        "quality_score": 89,
        "phone_score_list": [
          {
            "phone": "y",
            "stress_level": null,
            "extent": [
              83,
              107
            ],
            "quality_score": 74.625,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "s"
          },
          {
            "phone": "eh",
            "stress_level": 1,
            "extent": [
              107,
              119
            ],
            "quality_score": 93,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "eh"
          },
          {
            "phone": "s",
            "stress_level": null,
            "extent": [
              119,
              143
            ],
            "quality_score": 98.5,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "s"
          }
        ],
        "ending_punctuation": ".",
        "syllable_score_list": [
          {
            "phone_count": 3,
            "stress_level": 1,
            "letters": "yes",
            "quality_score": 89,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "extent": [
              83,
              143
            ]
          }
        ]
      },
      {
        "word": "said",
        "quality_score": 73,
        "phone_score_list": [
          {
            "phone": "s",
            "stress_level": null,
            "extent": [
              179,
              206
            ],
            "quality_score": 90.88888888888889,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "s"
          },
          {
            "phone": "eh",
            "stress_level": 1,
            "extent": [
              206,
              218
            ],
            "quality_score": 93.75,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "word_extent": [
              1,
              3
            ],
            "sound_most_like": "eh"
          },
          {
            "phone": "d",
            "stress_level": null,
            "extent": [
              218,
              224
            ],
            "quality_score": 35,
            "word_extent": [
              3,
              4
            ],
            "sound_most_like": "k"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 3,
            "stress_level": 1,
            "letters": "said",
            "quality_score": 73,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "extent": [
              179,
              224
            ]
          }
        ]
      },
      {
        "word": "Canine",
        "quality_score": 70,
        "phone_score_list": [
          {
            "phone": "k",
            "stress_level": null,
            "extent": [
              225,
              245
            ],
            "quality_score": 98.4,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "k"
          },
          {
            "phone": "ey",
            "stress_level": 1,
            "extent": [
              245,
              260
            ],
            "quality_score": 64.8,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "iy"
          },
          {
            "phone": "n",
            "stress_level": null,
            "extent": [
              260,
              266
            ],
            "quality_score": 95,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "n"
          },
          {
            "phone": "ay",
            "stress_level": 2,
            "extent": [
              266,
              266
            ],
            "quality_score": 0,
            "stress_score": 50,
            "predicted_stress_level": 0,
            "word_extent": [
              3,
              4
            ],
            "sound_most_like": null
          },
          {
            "phone": "n",
            "stress_level": null,
            "extent": [
              266,
              287
            ],
            "quality_score": 94.28571428571429,
            "word_extent": [
              4,
              6
            ],
            "sound_most_like": "n"
          }
        ],
        "ending_punctuation": "\u201c",
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "ca",
            "quality_score": 82,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              225,
              260
            ]
          },
          {
            "phone_count": 3,
            "stress_level": 2,
            "letters": "nine",
            "quality_score": 63,
            "stress_score": 50,
            "predicted_stress_level": 0,
            "extent": [
              260,
              287
            ]
          }
        ]
      },
      {
        "word": "I",
        "quality_score": 99,
        "phone_score_list": [
          {
            "phone": "ay",
            "stress_level": 1,
            "extent": [
              356,
              374
            ],
            "quality_score": 99.16666666666667,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "ay"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 1,
            "stress_level": 1,
            "letters": "i",
            "quality_score": 99,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              356,
              374
            ]
          }
        ]
      },
      {
        "word": "know",
        "quality_score": 94,
        "phone_score_list": [
          {
            "phone": "n",
            "stress_level": null,
            "extent": [
              374,
              386
            ],
            "quality_score": 99.5,
            "word_extent": [
              0,
              2
            ],
            "sound_most_like": "n"
          },
          {
            "phone": "ow",
            "stress_level": 1,
            "extent": [
              386,
              410
            ],
            "quality_score": 89.16666666666667,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              2,
              4
            ],
            "sound_most_like": "ow",
            "child_phones": [
              {
                "extent": [
                  386,
                  404
                ],
                "quality_score": 99.16666666666667,
                "sound_most_like": "ow"
              },
              {
                "extent": [
                  404,
                  407
                ],
                "quality_score": 18.333333333333325,
                "sound_most_like": "sil"
              },
              {
                "extent": [
                  407,
                  410
                ],
                "quality_score": 100,
                "sound_most_like": "ow"
              }
            ]
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "know",
            "quality_score": 94,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              374,
              410
            ]
          }
        ]
      },
      {
        "word": "exactly",
        "quality_score": 99,
        "phone_score_list": [
          {
            "phone": "ih",
            "stress_level": 0,
            "extent": [
              419,
              428
            ],
            "quality_score": 98.66666666666667,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "ih"
          },
          {
            "phone": "g",
            "stress_level": null,
            "extent": [
              428,
              434
            ],
            "quality_score": 100,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "g"
          },
          {
            "phone": "z",
            "stress_level": null,
            "extent": [
              434,
              443
            ],
            "quality_score": 100,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "z"
          },
          {
            "phone": "ae",
            "stress_level": 1,
            "extent": [
              443,
              455
            ],
            "quality_score": 99.75,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "ae"
          },
          {
            "phone": "k",
            "stress_level": null,
            "extent": [
              455,
              458
            ],
            "quality_score": 100,
            "word_extent": [
              3,
              4
            ],
            "sound_most_like": "k"
          },
          {
            "phone": "t",
            "stress_level": null,
            "extent": [
              458,
              464
            ],
            "quality_score": 98,
            "word_extent": [
              4,
              5
            ],
            "sound_most_like": "t"
          },
          {
            "phone": "l",
            "stress_level": null,
            "extent": [
              464,
              470
            ],
            "quality_score": 100,
            "word_extent": [
              5,
              6
            ],
            "sound_most_like": "l"
          },
          {
            "phone": "iy",
            "stress_level": 0,
            "extent": [
              470,
              482
            ],
            "quality_score": 97.75,
            "stress_score": 0,
            "predicted_stress_level": 1,
            "word_extent": [
              6,
              7
            ],
            "sound_most_like": "iy"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 0,
            "letters": "ex",
            "quality_score": 99,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "extent": [
              419,
              434
            ]
          },
          {
            "phone_count": 4,
            "stress_level": 1,
            "letters": "act",
            "quality_score": 99,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              434,
              464
            ]
          },
          {
            "phone_count": 2,
            "stress_level": 0,
            "letters": "ly",
            "quality_score": 99,
            "stress_score": 0,
            "predicted_stress_level": 1,
            "extent": [
              464,
              482
            ]
          }
        ]
      },
      {
        "word": "what's",
        "quality_score": 100,
        "phone_score_list": [
          {
            "phone": "w",
            "stress_level": null,
            "extent": [
              482,
              494
            ],
            "quality_score": 100,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "w"
          },
          {
            "phone": "ah",
            "stress_level": 1,
            "extent": [
              494,
              500
            ],
            "quality_score": 100,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "ah"
          },
          {
            "phone": "t",
            "stress_level": null,
            "extent": [
              500,
              506
            ],
            "quality_score": 100,
            "word_extent": [
              3,
              4
            ],
            "sound_most_like": "t"
          },
          {
            "phone": "s",
            "stress_level": null,
            "extent": [
              506,
              515
            ],
            "quality_score": 99,
            "word_extent": [
              5,
              6
            ],
            "sound_most_like": "s"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 4,
            "stress_level": 1,
            "letters": "what's",
            "quality_score": 100,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              482,
              515
            ]
          }
        ]
      },
      {
        "word": "wrong",
        "quality_score": 98,
        "phone_score_list": [
          {
            "phone": "r",
            "stress_level": null,
            "extent": [
              515,
              521
            ],
            "quality_score": 96,
            "word_extent": [
              0,
              2
            ],
            "sound_most_like": "r"
          },
          {
            "phone": "ao",
            "stress_level": 1,
            "extent": [
              521,
              530
            ],
            "quality_score": 100,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "ao"
          },
          {
            "phone": "ng",
            "stress_level": null,
            "extent": [
              530,
              542
            ],
            "quality_score": 99,
            "word_extent": [
              3,
              5
            ],
            "sound_most_like": "ng"
          }
        ],
        "ending_punctuation": ",",
        "syllable_score_list": [
          {
            "phone_count": 3,
            "stress_level": 1,
            "letters": "wrong",
            "quality_score": 98,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              515,
              542
            ]
          }
        ]
      },
      {
        "word": "The",
        "quality_score": 48,
        "phone_score_list": [
          {
            "phone": "dh",
            "stress_level": null,
            "extent": [
              542,
              542
            ],
            "quality_score": 0,
            "word_extent": [
              0,
              2
            ],
            "sound_most_like": null
          },
          {
            "phone": "ah",
            "stress_level": 0,
            "extent": [
              542,
              543
            ],
            "quality_score": 96,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "ah"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 0,
            "letters": "the",
            "quality_score": 48,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "extent": [
              542,
              543
            ]
          }
        ]
      },
      {
        "word": "children",
        "quality_score": 93,
        "phone_score_list": [
          {
            "phone": "ch",
            "stress_level": null,
            "extent": [
              608,
              617
            ],
            "quality_score": 100,
            "word_extent": [
              0,
              2
            ],
            "sound_most_like": "ch"
          },
          {
            "phone": "ih",
            "stress_level": 1,
            "extent": [
              617,
              623
            ],
            "quality_score": 97,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "ih"
          },
          {
            "phone": "l",
            "stress_level": null,
            "extent": [
              623,
              629
            ],
            "quality_score": 98,
            "word_extent": [
              3,
              4
            ],
            "sound_most_like": "l"
          },
          {
            "phone": "d",
            "stress_level": null,
            "extent": [
              629,
              630
            ],
            "quality_score": 82,
            "word_extent": [
              4,
              5
            ],
            "sound_most_like": "d"
          },
          {
            "phone": "r",
            "stress_level": null,
            "extent": [
              630,
              638
            ],
            "quality_score": 97,
            "word_extent": [
              5,
              6
            ],
            "sound_most_like": "r"
          },
          {
            "phone": "ah",
            "stress_level": 0,
            "extent": [
              638,
              639
            ],
            "quality_score": 80,
            "stress_score": 96,
            "predicted_stress_level": 1,
            "word_extent": [
              6,
              7
            ],
            "sound_most_like": "ah"
          },
          {
            "phone": "n",
            "stress_level": null,
            "extent": [
              639,
              653
            ],
            "quality_score": 97.85714285714286,
            "word_extent": [
              7,
              8
            ],
            "sound_most_like": "n"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 3,
            "stress_level": 1,
            "letters": "chil",
            "quality_score": 98,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              608,
              629
            ]
          },
          {
            "phone_count": 4,
            "stress_level": 0,
            "letters": "dren",
            "quality_score": 89,
            "stress_score": 96,
            "predicted_stress_level": 1,
            "extent": [
              629,
              653
            ]
          }
        ]
      },
      {
        "word": "are",
        "quality_score": 76,
        "phone_score_list": [
          {
            "phone": "aa",
            "stress_level": 1,
            "extent": [
              653,
              659
            ],
            "quality_score": 97,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "aa"
          },
          {
            "phone": "r",
            "stress_level": null,
            "extent": [
              659,
              664
            ],
            "quality_score": 54.66666666666667,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "ah",
            "child_phones": [
              {
                "extent": [
                  659,
                  662
                ],
                "quality_score": 90,
                "sound_most_like": "l"
              },
              {
                "extent": [
                  662,
                  664
                ],
                "quality_score": 1.6666666666666718,
                "sound_most_like": "ah"
              }
            ]
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "are",
            "quality_score": 76,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              653,
              664
            ]
          }
        ]
      },
      {
        "word": "beginning",
        "quality_score": 81,
        "phone_score_list": [
          {
            "phone": "b",
            "stress_level": null,
            "extent": [
              665,
              674
            ],
            "quality_score": 97.66666666666667,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "b"
          },
          {
            "phone": "ih",
            "stress_level": 0,
            "extent": [
              674,
              680
            ],
            "quality_score": 100,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "ih"
          },
          {
            "phone": "g",
            "stress_level": null,
            "extent": [
              680,
              683
            ],
            "quality_score": 94,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "g"
          },
          {
            "phone": "ih",
            "stress_level": 1,
            "extent": [
              683,
              683
            ],
            "quality_score": 0,
            "stress_score": 0,
            "predicted_stress_level": 0,
            "word_extent": [
              3,
              4
            ],
            "sound_most_like": null
          },
          {
            "phone": "n",
            "stress_level": null,
            "extent": [
              683,
              692
            ],
            "quality_score": 99.66666666666667,
            "word_extent": [
              5,
              6
            ],
            "sound_most_like": "n"
          },
          {
            "phone": "ih",
            "stress_level": 0,
            "extent": [
              692,
              695
            ],
            "quality_score": 91,
            "stress_score": 90,
            "predicted_stress_level": 1,
            "word_extent": [
              6,
              7
            ],
            "sound_most_like": "ih"
          },
          {
            "phone": "ng",
            "stress_level": null,
            "extent": [
              695,
              707
            ],
            "quality_score": 84.41666666666667,
            "word_extent": [
              7,
              9
            ],
            "sound_most_like": "ng",
            "child_phones": [
              {
                "extent": [
                  695,
                  704
                ],
                "quality_score": 98.66666666666667,
                "sound_most_like": "ng"
              },
              {
                "extent": [
                  704,
                  707
                ],
                "quality_score": 41.666666666666664,
                "sound_most_like": "g"
              }
            ]
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 0,
            "letters": "be",
            "quality_score": 99,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "extent": [
              665,
              680
            ]
          },
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "gin",
            "quality_score": 47,
            "stress_score": 0,
            "predicted_stress_level": 0,
            "extent": [
              680,
              683
            ]
          },
          {
            "phone_count": 3,
            "stress_level": 0,
            "letters": "ning",
            "quality_score": 92,
            "stress_score": 90,
            "predicted_stress_level": 1,
            "extent": [
              683,
              707
            ]
          }
        ]
      },
      {
        "word": "to",
        "quality_score": 95,
        "phone_score_list": [
          {
            "phone": "t",
            "stress_level": null,
            "extent": [
              707,
              710
            ],
            "quality_score": 92,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "t"
          },
          {
            "phone": "uw",
            "stress_level": 1,
            "extent": [
              710,
              722
            ],
            "quality_score": 98.5,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "uw"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "to",
            "quality_score": 95,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              707,
              722
            ]
          }
        ]
      },
      {
        "word": "eat",
        "quality_score": 98,
        "phone_score_list": [
          {
            "phone": "iy",
            "stress_level": 1,
            "extent": [
              725,
              746
            ],
            "quality_score": 99.42857142857143,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              0,
              2
            ],
            "sound_most_like": "iy"
          },
          {
            "phone": "t",
            "stress_level": null,
            "extent": [
              746,
              755
            ],
            "quality_score": 97.33333333333333,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "t"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "eat",
            "quality_score": 98,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              725,
              755
            ]
          }
        ]
      },
      {
        "word": "far",
        "quality_score": 100,
        "phone_score_list": [
          {
            "phone": "f",
            "stress_level": null,
            "extent": [
              803,
              812
            ],
            "quality_score": 100,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "f"
          },
          {
            "phone": "aa",
            "stress_level": 1,
            "extent": [
              812,
              824
            ],
            "quality_score": 100,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "aa"
          },
          {
            "phone": "r",
            "stress_level": null,
            "extent": [
              824,
              830
            ],
            "quality_score": 99.5,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "r"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 3,
            "stress_level": 1,
            "letters": "far",
            "quality_score": 100,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              803,
              830
            ]
          }
        ]
      },
      {
        "word": "too",
        "quality_score": 100,
        "phone_score_list": [
          {
            "phone": "t",
            "stress_level": null,
            "extent": [
              830,
              839
            ],
            "quality_score": 99.66666666666667,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "t"
          },
          {
            "phone": "uw",
            "stress_level": 1,
            "extent": [
              839,
              848
            ],
            "quality_score": 100,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              1,
              3
            ],
            "sound_most_like": "uw"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "too",
            "quality_score": 100,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              830,
              848
            ]
          }
        ]
      },
      {
        "word": "many",
        "quality_score": 97,
        "phone_score_list": [
          {
            "phone": "m",
            "stress_level": null,
            "extent": [
              848,
              857
            ],
            "quality_score": 97,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "m"
          },
          {
            "phone": "eh",
            "stress_level": 1,
            "extent": [
              857,
              860
            ],
            "quality_score": 94,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "eh"
          },
          {
            "phone": "n",
            "stress_level": null,
            "extent": [
              860,
              866
            ],
            "quality_score": 100,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "n"
          },
          {
            "phone": "iy",
            "stress_level": 0,
            "extent": [
              866,
              872
            ],
            "quality_score": 97.5,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "word_extent": [
              3,
              4
            ],
            "sound_most_like": "iy"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 3,
            "stress_level": 1,
            "letters": "man",
            "quality_score": 97,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              848,
              866
            ]
          },
          {
            "phone_count": 1,
            "stress_level": 0,
            "letters": "y",
            "quality_score": 98,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "extent": [
              866,
              872
            ]
          }
        ]
      },
      {
        "word": "sweets",
        "quality_score": 89,
        "phone_score_list": [
          {
            "phone": "s",
            "stress_level": null,
            "extent": [
              872,
              884
            ],
            "quality_score": 96,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "s"
          },
          {
            "phone": "w",
            "stress_level": null,
            "extent": [
              884,
              887
            ],
            "quality_score": 94,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "w"
          },
          {
            "phone": "iy",
            "stress_level": 1,
            "extent": [
              887,
              899
            ],
            "quality_score": 81.66666666666667,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              2,
              4
            ],
            "sound_most_like": "iy",
            "child_phones": [
              {
                "extent": [
                  887,
                  896
                ],
                "quality_score": 95,
                "sound_most_like": "iy"
              },
              {
                "extent": [
                  896,
                  899
                ],
                "quality_score": 41.666666666666664,
                "sound_most_like": "ah"
              }
            ]
          },
          {
            "phone": "t",
            "stress_level": null,
            "extent": [
              899,
              911
            ],
            "quality_score": 81.5,
            "word_extent": [
              4,
              5
            ],
            "sound_most_like": "t"
          },
          {
            "phone": "s",
            "stress_level": null,
            "extent": [
              911,
              923
            ],
            "quality_score": 91.5,
            "word_extent": [
              5,
              6
            ],
            "sound_most_like": "s"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 5,
            "stress_level": 1,
            "letters": "sweets",
            "quality_score": 89,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              872,
              923
            ]
          }
        ]
      },
      {
        "word": "and",
        "quality_score": 66,
        "phone_score_list": [
          {
            "phone": "ae",
            "stress_level": 1,
            "extent": [
              953,
              959
            ],
            "quality_score": 99.5,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "ae"
          },
          {
            "phone": "n",
            "stress_level": null,
            "extent": [
              959,
              965
            ],
            "quality_score": 99.5,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "n"
          },
          {
            "phone": "d",
            "stress_level": null,
            "extent": [
              965,
              965
            ],
            "quality_score": 0,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": null
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 3,
            "stress_level": 1,
            "letters": "and",
            "quality_score": 66,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              953,
              965
            ]
          }
        ]
      },
      {
        "word": "are",
        "quality_score": 66,
        "phone_score_list": [
          {
            "phone": "aa",
            "stress_level": 1,
            "extent": [
              966,
              971
            ],
            "quality_score": 97.6,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "aa"
          },
          {
            "phone": "r",
            "stress_level": null,
            "extent": [
              971,
              972
            ],
            "quality_score": 35,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "n"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "are",
            "quality_score": 66,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              966,
              972
            ]
          }
        ]
      },
      {
        "word": "not",
        "quality_score": 75,
        "phone_score_list": [
          {
            "phone": "n",
            "stress_level": null,
            "extent": [
              972,
              986
            ],
            "quality_score": 96.78571428571429,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "n"
          },
          {
            "phone": "aa",
            "stress_level": 1,
            "extent": [
              986,
              995
            ],
            "quality_score": 94.33333333333333,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "aa"
          },
          {
            "phone": "t",
            "stress_level": null,
            "extent": [
              995,
              1001
            ],
            "quality_score": 35,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "n"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 3,
            "stress_level": 1,
            "letters": "not",
            "quality_score": 75,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              972,
              1001
            ]
          }
        ]
      },
      {
        "word": "looking",
        "quality_score": 99,
        "phone_score_list": [
          {
            "phone": "l",
            "stress_level": null,
            "extent": [
              1001,
              1007
            ],
            "quality_score": 99,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "l"
          },
          {
            "phone": "uh",
            "stress_level": 1,
            "extent": [
              1007,
              1016
            ],
            "quality_score": 98.66666666666667,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              1,
              3
            ],
            "sound_most_like": "uh"
          },
          {
            "phone": "k",
            "stress_level": null,
            "extent": [
              1016,
              1022
            ],
            "quality_score": 100,
            "word_extent": [
              3,
              4
            ],
            "sound_most_like": "k"
          },
          {
            "phone": "ih",
            "stress_level": 0,
            "extent": [
              1022,
              1028
            ],
            "quality_score": 99.5,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "word_extent": [
              4,
              5
            ],
            "sound_most_like": "ih"
          },
          {
            "phone": "ng",
            "stress_level": null,
            "extent": [
              1028,
              1034
            ],
            "quality_score": 100,
            "word_extent": [
              5,
              7
            ],
            "sound_most_like": "ng"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 3,
            "stress_level": 1,
            "letters": "look",
            "quality_score": 99,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              1001,
              1022
            ]
          },
          {
            "phone_count": 2,
            "stress_level": 0,
            "letters": "ing",
            "quality_score": 100,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "extent": [
              1022,
              1034
            ]
          }
        ]
      },
      {
        "word": "after",
        "quality_score": 96,
        "phone_score_list": [
          {
            "phone": "ae",
            "stress_level": 1,
            "extent": [
              1034,
              1043
            ],
            "quality_score": 95,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "ae"
          },
          {
            "phone": "f",
            "stress_level": null,
            "extent": [
              1043,
              1052
            ],
            "quality_score": 98.66666666666667,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "f"
          },
          {
            "phone": "t",
            "stress_level": null,
            "extent": [
              1052,
              1055
            ],
            "quality_score": 96,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "t"
          },
          {
            "phone": "er",
            "stress_level": 0,
            "extent": [
              1055,
              1064
            ],
            "quality_score": 92.33333333333333,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "word_extent": [
              3,
              5
            ],
            "sound_most_like": "er"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "af",
            "quality_score": 97,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              1034,
              1052
            ]
          },
          {
            "phone_count": 2,
            "stress_level": 0,
            "letters": "ter",
            "quality_score": 94,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "extent": [
              1052,
              1064
            ]
          }
        ]
      },
      {
        "word": "their",
        "quality_score": 76,
        "phone_score_list": [
          {
            "phone": "dh",
            "stress_level": null,
            "extent": [
              1064,
              1070
            ],
            "quality_score": 100,
            "word_extent": [
              0,
              2
            ],
            "sound_most_like": "dh"
          },
          {
            "phone": "eh",
            "stress_level": 1,
            "extent": [
              1070,
              1079
            ],
            "quality_score": 94,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "eh"
          },
          {
            "phone": "r",
            "stress_level": null,
            "extent": [
              1079,
              1080
            ],
            "quality_score": 35,
            "word_extent": [
              4,
              5
            ],
            "sound_most_like": "f"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 3,
            "stress_level": 1,
            "letters": "their",
            "quality_score": 76,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "extent": [
              1064,
              1080
            ]
          }
        ]
      },
      {
        "word": "teeth",
        "quality_score": 71,
        "phone_score_list": [
          {
            "phone": "t",
            "stress_level": null,
            "extent": [
              1080,
              1094
            ],
            "quality_score": 79.64285714285714,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "v",
            "child_phones": [
              {
                "extent": [
                  1080,
                  1082
                ],
                "quality_score": 91,
                "sound_most_like": "f"
              },
              {
                "extent": [
                  1082,
                  1085
                ],
                "quality_score": 35,
                "sound_most_like": "v"
              },
              {
                "extent": [
                  1085,
                  1094
                ],
                "quality_score": 92,
                "sound_most_like": "d"
              }
            ]
          },
          {
            "phone": "iy",
            "stress_level": 1,
            "extent": [
              1094,
              1106
            ],
            "quality_score": 99,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              1,
              3
            ],
            "sound_most_like": "iy"
          },
          {
            "phone": "th",
            "stress_level": null,
            "extent": [
              1106,
              1115
            ],
            "quality_score": 34.999999999999986,
            "word_extent": [
              3,
              5
            ],
            "sound_most_like": "t"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 3,
            "stress_level": 1,
            "letters": "teeth",
            "quality_score": 71,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              1080,
              1115
            ]
          }
        ]
      },
      {
        "word": "at",
        "quality_score": 73,
        "phone_score_list": [
          {
            "phone": "ae",
            "stress_level": 1,
            "extent": [
              1115,
              1124
            ],
            "quality_score": 92.66666666666667,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "ae"
          },
          {
            "phone": "t",
            "stress_level": null,
            "extent": [
              1124,
              1133
            ],
            "quality_score": 53.333333333333336,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "th"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "at",
            "quality_score": 73,
            "stress_score": 100,
            "predicted_stress_level": 0,
            "extent": [
              1115,
              1133
            ]
          }
        ]
      },
      {
        "word": "all",
        "quality_score": 53,
        "phone_score_list": [
          {
            "phone": "ao",
            "stress_level": 1,
            "extent": [
              1133,
              1142
            ],
            "quality_score": 98.33333333333333,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              0,
              2
            ],
            "sound_most_like": "ao"
          },
          {
            "phone": "l",
            "stress_level": null,
            "extent": [
              1142,
              1157
            ],
            "quality_score": 7.616666666666666,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "ah",
            "child_phones": [
              {
                "extent": [
                  1142,
                  1145
                ],
                "quality_score": 24.75,
                "sound_most_like": "l"
              },
              {
                "extent": [
                  1145,
                  1148
                ],
                "quality_score": 0,
                "sound_most_like": "ah"
              },
              {
                "extent": [
                  1148,
                  1151
                ],
                "quality_score": 0,
                "sound_most_like": "er"
              },
              {
                "extent": [
                  1151,
                  1154
                ],
                "quality_score": 8.75,
                "sound_most_like": "t"
              },
              {
                "extent": [
                  1154,
                  1157
                ],
                "quality_score": 4.583333333333331,
                "sound_most_like": "iy"
              }
            ]
          }
        ],
        "ending_punctuation": ".",
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "all",
            "quality_score": 53,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              1133,
              1157
            ]
          }
        ]
      },
      {
        "word": "I",
        "quality_score": 0,
        "phone_score_list": [
          {
            "phone": "ay",
            "stress_level": 1,
            "extent": [
              1159,
              1159
            ],
            "quality_score": 0,
            "stress_score": 0,
            "predicted_stress_level": 0,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": null
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 1,
            "stress_level": 1,
            "letters": "i",
            "quality_score": 0,
            "stress_score": 0,
            "predicted_stress_level": 0,
            "extent": [
              1159,
              1159
            ]
          }
        ]
      },
      {
        "word": "know",
        "quality_score": 47,
        "phone_score_list": [
          {
            "phone": "n",
            "stress_level": null,
            "extent": [
              1160,
              1163
            ],
            "quality_score": 94,
            "word_extent": [
              0,
              2
            ],
            "sound_most_like": "n"
          },
          {
            "phone": "ow",
            "stress_level": 1,
            "extent": [
              1163,
              1163
            ],
            "quality_score": 0,
            "stress_score": 0,
            "predicted_stress_level": 0,
            "word_extent": [
              2,
              4
            ],
            "sound_most_like": null
          }
        ],
        "ending_punctuation": "\u2026",
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "know",
            "quality_score": 47,
            "stress_score": 0,
            "predicted_stress_level": 0,
            "extent": [
              1160,
              1163
            ]
          }
        ]
      },
      {
        "word": "we",
        "quality_score": 23,
        "phone_score_list": [
          {
            "phone": "w",
            "stress_level": null,
            "extent": [
              1234,
              1235
            ],
            "quality_score": 0,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "ih"
          },
          {
            "phone": "iy",
            "stress_level": 1,
            "extent": [
              1235,
              1236
            ],
            "quality_score": 45.833333333333336,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "ih"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "we",
            "quality_score": 23,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              1234,
              1236
            ]
          }
        ]
      },
      {
        "word": "can",
        "quality_score": 64,
        "phone_score_list": [
          {
            "phone": "k",
            "stress_level": null,
            "extent": [
              1236,
              1236
            ],
            "quality_score": 0,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": null
          },
          {
            "phone": "ah",
            "stress_level": 0,
            "extent": [
              1236,
              1238
            ],
            "quality_score": 96,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "ah"
          },
          {
            "phone": "n",
            "stress_level": null,
            "extent": [
              1238,
              1241
            ],
            "quality_score": 95,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "n"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 3,
            "stress_level": 0,
            "letters": "can",
            "quality_score": 64,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              1236,
              1241
            ]
          }
        ]
      },
      {
        "word": "fix",
        "quality_score": 49,
        "phone_score_list": [
          {
            "phone": "f",
            "stress_level": null,
            "extent": [
              1241,
              1241
            ],
            "quality_score": 0,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": null
          },
          {
            "phone": "ih",
            "stress_level": 1,
            "extent": [
              1241,
              1241
            ],
            "quality_score": 0,
            "stress_score": 0,
            "predicted_stress_level": 0,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": null
          },
          {
            "phone": "k",
            "stress_level": null,
            "extent": [
              1241,
              1244
            ],
            "quality_score": 100,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "k"
          },
          {
            "phone": "s",
            "stress_level": null,
            "extent": [
              1244,
              1256
            ],
            "quality_score": 94.25,
            "word_extent": [
              2,
              3
            ],
            "sound_most_like": "s"
          }
        ],
        "syllable_score_list": [
          {
            "phone_count": 4,
            "stress_level": 1,
            "letters": "fix",
            "quality_score": 49,
            "stress_score": 0,
            "predicted_stress_level": 0,
            "extent": [
              1241,
              1256
            ]
          }
        ]
      },
      {
        "word": "it",
        "quality_score": 40,
        "phone_score_list": [
          {
            "phone": "ih",
            "stress_level": 1,
            "extent": [
              1256,
              1268
            ],
            "quality_score": 45.833333333333314,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "word_extent": [
              0,
              1
            ],
            "sound_most_like": "iy"
          },
          {
            "phone": "t",
            "stress_level": null,
            "extent": [
              1268,
              1274
            ],
            "quality_score": 35,
            "word_extent": [
              1,
              2
            ],
            "sound_most_like": "m",
            "child_phones": [
              {
                "extent": [
                  1268,
                  1271
                ],
                "quality_score": 35,
                "sound_most_like": "n"
              },
              {
                "extent": [
                  1271,
                  1274
                ],
                "quality_score": 35,
                "sound_most_like": "m"
              }
            ]
          }
        ],
        "ending_punctuation": "!",
        "syllable_score_list": [
          {
            "phone_count": 2,
            "stress_level": 1,
            "letters": "it",
            "quality_score": 40,
            "stress_score": 100,
            "predicted_stress_level": 1,
            "extent": [
              1256,
              1274
            ]
          }
        ]
      }
    ],
    "ielts_score": {
      "pronunciation": 7.5
    },
    "pte_score": {
      "pronunciation": 72
    },
    "speechace_score": {
      "pronunciation": 81
    },
    "toeic_score": {
      "pronunciation": 170
    },
    "cefr_score": {
      "pronunciation": "C1"
    }
  },
  "version": "9.9"
}


def simplify_json(data):
    words = data['text_score']['word_score_list']
    # Calculate the average quality score of all words
    total_quality_score = sum(word['quality_score'] for word in words)
    average_quality_score = total_quality_score / len(words)

    simplified_data = []

    for word_info in words:
        if word_info['quality_score'] < average_quality_score and len(word_info['word']) >= 4:
            word_entry = {
                'word': word_info['word'],
                'context': {
                    'previous_word': None,  # Update these based on your data's sequence
                    'next_word': None
                },
                'phonetics': []
            }

            for phone_info in word_info.get('phone_score_list', []):
                if phone_info['sound_most_like'] and phone_info['sound_most_like'] != phone_info['phone']:
                    phonetic_entry = {
                        'actual_phonetic': phone_info['phone'],
                        'almost_sounds_like_phonetic': phone_info['sound_most_like'],
                        'stress_level': phone_info.get('stress_level'),
                        'predicted_stress_level': phone_info.get('predicted_stress_level')
                    }
                    word_entry['phonetics'].append(phonetic_entry)

            # Add context
            word_index = words.index(word_info)
            if word_index > 0:
                word_entry['context']['previous_word'] = words[word_index - 1]['word']
            if word_index < len(words) - 1:
                word_entry['context']['next_word'] = words[word_index + 1]['word']

            simplified_data.append(word_entry)

    return simplified_data

# Use the function on the provided JSON
simplified_json = simplify_json(api_response)

# Printing the simplified JSON
print(json.dumps(simplified_json, indent=4))

# Optionally, convert it back to JSON string if you need to pass it elsewhere
simplified_json_str = json.dumps(simplified_json)