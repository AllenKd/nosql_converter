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
    "_id" : NumberInt(6896), 
    "game_id" : NumberInt(6896), 
    "game_time" : "2020-01-27T10:00", 
    "gamble_id" : NumberInt(454), 
    "game_type" : "NBA", 
    "guest" : {
        "name" : "IND", 
        "score" : NumberInt(129)
    }, 
    "host" : {
        "name" : "POR", 
        "score" : NumberInt(139)
    }, 
    "gamble_info" : {
        "national" : {
            "total_point" : {
                "threshold" : 221.0
            }, 
            "spread_point" : {
                "host" : NumberInt(3), 
                "response" : {
                    "on_hit" : 1.5
                }
            }
        }, 
        "local" : {
            "total_point" : {
                "threshold" : 221.5, 
                "response" : 1.7
            }, 
            "spread_point" : {
                "host" : 1.5, 
                "response" : {
                    "host" : 1.8
                }
            }, 
            "original" : {
                "response" : {
                    "guest" : 1.85, 
                    "host" : 1.65
                }
            }
        }
    }, 
    "judgement" : {
        "game" : {
            "national" : {
                "over_threshold" : false, 
                "spread_point" : "guest"
            }, 
            "local" : {
                "over_threshold" : false, 
                "spread_point" : "guest", 
                "original" : "guest"
            }
        }, 
        "prediction" : [
            {
                "group" : "all_member", 
                "national" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }, 
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }
                }, 
                "local" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }, 
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }, 
                    "original" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }
                }
            }, 
            {
                "group" : "all_prefer", 
                "national" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }, 
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }
                }, 
                "local" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }, 
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }, 
                    "original" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }
                }
            }, 
            {
                "group" : "more_than_sixty", 
                "national" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }, 
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }
                }, 
                "local" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }, 
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }, 
                    "original" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }
                }
            }, 
            {
                "group" : "top_100", 
                "national" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }, 
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }
                }, 
                "local" : {
                    "total_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }, 
                    "spread_point" : {
                        "matched_info" : {
                            "is_major" : false
                        }
                    }, 
                    "original" : {
                        "matched_info" : {
                            "is_major" : false
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
                        "percentage" : NumberInt(63), 
                        "population" : NumberInt(312)
                    }, 
                    "under" : {
                        "percentage" : NumberInt(37), 
                        "population" : NumberInt(187)
                    }
                }, 
                "spread_point" : {
                    "guest" : {
                        "percentage" : NumberInt(55), 
                        "population" : NumberInt(720)
                    }, 
                    "host" : {
                        "percentage" : NumberInt(45), 
                        "population" : NumberInt(599)
                    }
                }
            }, 
            "local" : {
                "total_point" : {
                    "over" : {
                        "percentage" : NumberInt(60), 
                        "population" : NumberInt(234)
                    }, 
                    "under" : {
                        "percentage" : NumberInt(40), 
                        "population" : NumberInt(153)
                    }
                }, 
                "spread_point" : {
                    "guest" : {
                        "percentage" : NumberInt(54), 
                        "population" : NumberInt(515)
                    }, 
                    "host" : {
                        "percentage" : NumberInt(46), 
                        "population" : NumberInt(433)
                    }
                }, 
                "original" : {
                    "guest" : {
                        "percentage" : NumberInt(49), 
                        "population" : NumberInt(171)
                    }, 
                    "host" : {
                        "percentage" : NumberInt(51), 
                        "population" : NumberInt(175)
                    }
                }
            }
        }, 
        {
            "group" : "all_prefer", 
            "national" : {
                "total_point" : {
                    "over" : {
                        "percentage" : NumberInt(67), 
                        "population" : NumberInt(42)
                    }, 
                    "under" : {
                        "percentage" : NumberInt(33), 
                        "population" : NumberInt(21)
                    }
                }, 
                "spread_point" : {
                    "guest" : {
                        "percentage" : NumberInt(45), 
                        "population" : NumberInt(115)
                    }, 
                    "host" : {
                        "percentage" : NumberInt(55), 
                        "population" : NumberInt(142)
                    }
                }
            }, 
            "local" : {
                "total_point" : {
                    "over" : {
                        "percentage" : NumberInt(59), 
                        "population" : NumberInt(44)
                    }, 
                    "under" : {
                        "percentage" : NumberInt(41), 
                        "population" : NumberInt(30)
                    }
                }, 
                "spread_point" : {
                    "guest" : {
                        "percentage" : NumberInt(49), 
                        "population" : NumberInt(104)
                    }, 
                    "host" : {
                        "percentage" : NumberInt(51), 
                        "population" : NumberInt(109)
                    }
                }, 
                "original" : {
                    "guest" : {
                        "percentage" : NumberInt(0), 
                        "population" : NumberInt(0)
                    }, 
                    "host" : {
                        "percentage" : NumberInt(0), 
                        "population" : NumberInt(0)
                    }
                }
            }
        }, 
        {
            "group" : "more_than_sixty", 
            "national" : {
                "total_point" : {
                    "over" : {
                        "percentage" : NumberInt(60), 
                        "population" : NumberInt(9)
                    }, 
                    "under" : {
                        "percentage" : NumberInt(40), 
                        "population" : NumberInt(6)
                    }
                }, 
                "spread_point" : {
                    "guest" : {
                        "percentage" : NumberInt(69), 
                        "population" : NumberInt(22)
                    }, 
                    "host" : {
                        "percentage" : NumberInt(31), 
                        "population" : NumberInt(10)
                    }
                }
            }, 
            "local" : {
                "total_point" : {
                    "over" : {
                        "percentage" : NumberInt(50), 
                        "population" : NumberInt(3)
                    }, 
                    "under" : {
                        "percentage" : NumberInt(50), 
                        "population" : NumberInt(3)
                    }
                }, 
                "spread_point" : {
                    "guest" : {
                        "percentage" : NumberInt(70), 
                        "population" : NumberInt(21)
                    }, 
                    "host" : {
                        "percentage" : NumberInt(30), 
                        "population" : NumberInt(9)
                    }
                }, 
                "original" : {
                    "guest" : {
                        "percentage" : NumberInt(57), 
                        "population" : NumberInt(40)
                    }, 
                    "host" : {
                        "percentage" : NumberInt(43), 
                        "population" : NumberInt(30)
                    }
                }
            }
        }, 
        {
            "group" : "top_100", 
            "national" : {
                "total_point" : {
                    "over" : {
                        "percentage" : NumberInt(62), 
                        "population" : NumberInt(24)
                    }, 
                    "under" : {
                        "percentage" : NumberInt(38), 
                        "population" : NumberInt(15)
                    }
                }, 
                "spread_point" : {
                    "guest" : {
                        "percentage" : NumberInt(69), 
                        "population" : NumberInt(29)
                    }, 
                    "host" : {
                        "percentage" : NumberInt(31), 
                        "population" : NumberInt(13)
                    }
                }
            }, 
            "local" : {
                "total_point" : {
                    "over" : {
                        "percentage" : NumberInt(61), 
                        "population" : NumberInt(20)
                    }, 
                    "under" : {
                        "percentage" : NumberInt(39), 
                        "population" : NumberInt(13)
                    }
                }, 
                "spread_point" : {
                    "guest" : {
                        "percentage" : NumberInt(60), 
                        "population" : NumberInt(25)
                    }, 
                    "host" : {
                        "percentage" : NumberInt(40), 
                        "population" : NumberInt(17)
                    }
                }, 
                "original" : {
                    "guest" : {
                        "percentage" : NumberInt(58), 
                        "population" : NumberInt(22)
                    }, 
                    "host" : {
                        "percentage" : NumberInt(42), 
                        "population" : NumberInt(16)
                    }
                }
            }
        }
    ]
}

```

