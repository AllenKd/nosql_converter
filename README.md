# NoSQL Converter

To convert SQL data from [Crawler](https://github.com/AllenKd/sports_data_crawler) to JSON format then store into MongoDB.

## Docker Image

```
$ docker pull allensyk/nosql_converter
```

| Environment Variable | Description |
| :--- | :--- |
| DB_HOST | DB host address. |
| DB_PORT | DB port. |
| DB_USERNAME | DB username. |
| DB_PASSWORD | DB user password. |
| MONGO_HOST | MongoDB host address. |
| MONGO_PORT | MongoDB port. |

## Converted JSON Document Example

```
{
    "_id" : ObjectId("5e9dc4498db98f99c86d1393"),
    "game_id" : 911,
    "game_time" : "2018-09-29T07:30",
    "gamble_id" : 360.0,
    "game_type" : "NBA",
    "guest" : {
        "name" : "BOS",
        "score" : 97
    },
    "host" : {
        "name" : "CHA",
        "score" : 104
    },
    "gamble_info" : {
        "national" : {
            "total_point" : {
                "threshold" : 207.0
            },
            "spread_point" : {
                "host" : -5.0,
                "response" : {
                    "on_hit" : 0.5
                }
            }
        },
        "local" : {
            "total_point" : {
                "threshold" : 207.5,
                "response" : {
                    "under" : 1.75,
                    "over" : 1.75
                }
            },
            "spread_point" : {
                "host" : -6.5,
                "response" : {
                    "host" : 1.75,
                    "guest" : 1.75
                }
            },
            "original" : {
                "response" : {
                    "guest" : 0.0,
                    "host" : 0.0
                }
            }
        }
    },
    "judgement" : {
        "game" : {
            "national" : {
                "total_point" : false,
                "spread_point" : "host"
            },
            "local" : {
                "total_point" : false,
                "spread_point" : "host",
                "original" : "host"
            }
        },
        "prediction" : [ 
            {
                "group" : "all_member",
                "national" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : true,
                            "percentage" : 55.0,
                            "population" : 370.0
                        }
                    },
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 39.0,
                            "population" : 375.0
                        }
                    }
                },
                "local" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : true,
                            "percentage" : 66.0,
                            "population" : 327.0
                        }
                    },
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 43.0,
                            "population" : 290.0
                        }
                    },
                    "original" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 0.0,
                            "population" : 0.0
                        }
                    }
                }
            }, 
            {
                "group" : "all_prefer",
                "national" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : true,
                            "percentage" : 52.0,
                            "population" : 171.0
                        }
                    },
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 40.0,
                            "population" : 256.0
                        }
                    }
                },
                "local" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : true,
                            "percentage" : 72.0,
                            "population" : 190.0
                        }
                    },
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 42.0,
                            "population" : 184.0
                        }
                    },
                    "original" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 0.0,
                            "population" : 0.0
                        }
                    }
                }
            }, 
            {
                "group" : "more_than_sixty",
                "national" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 40.0,
                            "population" : 2.0
                        }
                    },
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 40.0,
                            "population" : 2.0
                        }
                    }
                },
                "local" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : true,
                            "percentage" : 0.0,
                            "population" : 0.0
                        }
                    },
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 0.0,
                            "population" : 0.0
                        }
                    },
                    "original" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 0.0,
                            "population" : 0.0
                        }
                    }
                }
            }, 
            {
                "group" : "top_100",
                "national" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 25.0,
                            "population" : 1.0
                        }
                    },
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 50.0,
                            "population" : 1.0
                        }
                    }
                },
                "local" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : true,
                            "percentage" : 0.0,
                            "population" : 0.0
                        }
                    },
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 0.0,
                            "population" : 0.0
                        }
                    },
                    "original" : {
                        "matched_info" : {
                            "is_major" : false,
                            "percentage" : 0.0,
                            "population" : 0.0
                        }
                    }
                }
            }
        ]
    },
    "prediction" : [ 
        {
            "group" : "all_member",
            "national" : {
                "total_point" : {
                    "over" : {
                        "percentage" : 45,
                        "population" : 299
                    },
                    "under" : {
                        "percentage" : 55,
                        "population" : 370
                    }
                },
                "spread_point" : {
                    "guest" : {
                        "percentage" : 61,
                        "population" : 593
                    },
                    "host" : {
                        "percentage" : 39,
                        "population" : 375
                    }
                }
            },
            "local" : {
                "total_point" : {
                    "over" : {
                        "percentage" : 34,
                        "population" : 167
                    },
                    "under" : {
                        "percentage" : 66,
                        "population" : 327
                    }
                },
                "spread_point" : {
                    "guest" : {
                        "percentage" : 57,
                        "population" : 391
                    },
                    "host" : {
                        "percentage" : 43,
                        "population" : 290
                    }
                },
                "original" : {
                    "guest" : {
                        "percentage" : 0,
                        "population" : 0
                    },
                    "host" : {
                        "percentage" : 0,
                        "population" : 0
                    }
                }
            }
        }, 
        {
            "group" : "all_prefer",
            "national" : {
                "total_point" : {
                    "over" : {
                        "percentage" : 48,
                        "population" : 155
                    },
                    "under" : {
                        "percentage" : 52,
                        "population" : 171
                    }
                },
                "spread_point" : {
                    "guest" : {
                        "percentage" : 60,
                        "population" : 381
                    },
                    "host" : {
                        "percentage" : 40,
                        "population" : 256
                    }
                }
            },
            "local" : {
                "total_point" : {
                    "over" : {
                        "percentage" : 28,
                        "population" : 74
                    },
                    "under" : {
                        "percentage" : 72,
                        "population" : 190
                    }
                },
                "spread_point" : {
                    "guest" : {
                        "percentage" : 58,
                        "population" : 251
                    },
                    "host" : {
                        "percentage" : 42,
                        "population" : 184
                    }
                },
                "original" : {
                    "guest" : {
                        "percentage" : 0,
                        "population" : 0
                    },
                    "host" : {
                        "percentage" : 0,
                        "population" : 0
                    }
                }
            }
        }, 
        {
            "group" : "more_than_sixty",
            "national" : {
                "total_point" : {
                    "over" : {
                        "percentage" : 60,
                        "population" : 3
                    },
                    "under" : {
                        "percentage" : 40,
                        "population" : 2
                    }
                },
                "spread_point" : {
                    "guest" : {
                        "percentage" : 60,
                        "population" : 3
                    },
                    "host" : {
                        "percentage" : 40,
                        "population" : 2
                    }
                }
            },
            "local" : {
                "total_point" : {
                    "over" : {
                        "percentage" : 0,
                        "population" : 0
                    },
                    "under" : {
                        "percentage" : 0,
                        "population" : 0
                    }
                },
                "spread_point" : {
                    "guest" : {
                        "percentage" : 0,
                        "population" : 0
                    },
                    "host" : {
                        "percentage" : 0,
                        "population" : 0
                    }
                },
                "original" : {
                    "guest" : {
                        "percentage" : 0,
                        "population" : 0
                    },
                    "host" : {
                        "percentage" : 0,
                        "population" : 0
                    }
                }
            }
        }, 
        {
            "group" : "top_100",
            "national" : {
                "total_point" : {
                    "over" : {
                        "percentage" : 75,
                        "population" : 3
                    },
                    "under" : {
                        "percentage" : 25,
                        "population" : 1
                    }
                },
                "spread_point" : {
                    "guest" : {
                        "percentage" : 50,
                        "population" : 1
                    },
                    "host" : {
                        "percentage" : 50,
                        "population" : 1
                    }
                }
            },
            "local" : {
                "total_point" : {
                    "over" : {
                        "percentage" : 0,
                        "population" : 0
                    },
                    "under" : {
                        "percentage" : 0,
                        "population" : 0
                    }
                },
                "spread_point" : {
                    "guest" : {
                        "percentage" : 0,
                        "population" : 0
                    },
                    "host" : {
                        "percentage" : 0,
                        "population" : 0
                    }
                },
                "original" : {
                    "guest" : {
                        "percentage" : 0,
                        "population" : 0
                    },
                    "host" : {
                        "percentage" : 0,
                        "population" : 0
                    }
                }
            }
        }
    ]
}
```

