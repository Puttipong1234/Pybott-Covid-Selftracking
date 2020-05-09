def คำถามอาการไข้():
  คำถามอาการไข้ = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "image",
          "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th.appspot.com/o/doctor%20(1).png?alt=media&token=74e146ed-e391-4cc6-95cf-6c58fc1032ca"
        },
        {
          "type": "text",
          "text": "Diagnos Question 1",
          "margin": "xl",
          "size": "lg",
          "align": "center",
          "weight": "bold",
          "color": "#FFFFFF"
        }
      ]
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "ข้อที่ 1",
              "size": "sm",
              "weight": "bold",
              "color": "#3F72AF"
            },
            {
              "type": "text",
              "text": "ท่านมีอาการไข้ขึ้นสูงหรือไม่คะ?",
              "size": "sm",
              "weight": "bold"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "xxl",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ไม่มีอาการ",
                    "text": "0"
                  },
                  "color": "#F9F7F7",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อยมาก",
                    "text": "1"
                  },
                  "color": "#F9F7F7",
                  "height": "sm",
                  "style": "secondary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "md",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อย",
                    "text": "2"
                  },
                  "color": "#DBE2EF",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ปานกลาง",
                    "text": "3"
                  },
                  "color": "#DBE2EF",
                  "height": "sm",
                  "style": "secondary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "md",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มาก",
                    "text": "4"
                  },
                  "color": "#3F72AF",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มากที่สุด",
                    "text": "5"
                  },
                  "color": "#112D4E",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "text",
              "text": "กรุณากรอกตามความเป็นจริงนะคะ",
              "margin": "lg",
              "size": "xs",
              "align": "end",
              "weight": "bold"
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "margin": "xl",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "margin": "xxl",
          "contents": [
            {
              "type": "text",
              "text": "ขอขอบพระคุณเป็นอย่างสูงที่ให้ความร่วมมือกับน้องหมอนะคะ",
              "margin": "xl",
              "align": "center",
              "weight": "bold",
              "color": "#FFFFFF",
              "wrap": True
            }
          ]
        }
      ]
    },
    "styles": {
      "header": {
        "backgroundColor": "#3F72AF"
      },
      "footer": {
        "backgroundColor": "#3F72AF"
      }
    }
  }
}
  return คำถามอาการไข้


คำถามอาการไอ = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "image",
          "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th.appspot.com/o/doctor%20(1).png?alt=media&token=74e146ed-e391-4cc6-95cf-6c58fc1032ca"
        },
        {
          "type": "text",
          "text": "Diagnos Question 2",
          "margin": "xl",
          "size": "lg",
          "align": "center",
          "weight": "bold",
          "color": "#FFFFFF"
        }
      ]
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "ข้อที่ 2",
              "size": "sm",
              "weight": "bold",
              "color": "#3F72AF"
            },
            {
              "type": "text",
              "text": "ท่านมีอาการไอแห้งหรือไม่คะ?",
              "size": "sm",
              "weight": "bold"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "xxl",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ไม่มีอาการ",
                    "text": "0"
                  },
                  "color": "#F9F7F7",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อยมาก",
                    "text": "1"
                  },
                  "color": "#F9F7F7",
                  "height": "sm",
                  "style": "secondary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "md",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อย",
                    "text": "2"
                  },
                  "color": "#DBE2EF",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ปานกลาง",
                    "text": "3"
                  },
                  "color": "#DBE2EF",
                  "height": "sm",
                  "style": "secondary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "md",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มาก",
                    "text": "4"
                  },
                  "color": "#3F72AF",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มากที่สุด",
                    "text": "5"
                  },
                  "color": "#112D4E",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "text",
              "text": "กรุณากรอกตามความเป็นจริงนะคะ",
              "margin": "lg",
              "size": "xs",
              "align": "end",
              "weight": "bold"
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "margin": "xl",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "margin": "xxl",
          "contents": [
            {
              "type": "text",
              "text": "ขอขอบพระคุณเป็นอย่างสูงที่ให้ความร่วมมือกับน้องหมอนะคะ",
              "margin": "xl",
              "align": "center",
              "weight": "bold",
              "color": "#FFFFFF",
              "wrap": True
            }
          ]
        }
      ]
    },
    "styles": {
      "header": {
        "backgroundColor": "#3F72AF"
      },
      "footer": {
        "backgroundColor": "#3F72AF"
      }
    }
  }
}

คำถามอาการเจ็บคอ =  {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "image",
          "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th.appspot.com/o/doctor%20(1).png?alt=media&token=74e146ed-e391-4cc6-95cf-6c58fc1032ca"
        },
        {
          "type": "text",
          "text": "Diagnos Question 3",
          "margin": "xl",
          "size": "lg",
          "align": "center",
          "weight": "bold",
          "color": "#FFFFFF"
        }
      ]
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "ข้อที่ 3",
              "size": "sm",
              "weight": "bold",
              "color": "#3F72AF"
            },
            {
              "type": "text",
              "text": "ท่านมีอาการเจ็บคอหรือไม่คะ?",
              "size": "sm",
              "weight": "bold"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "xxl",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ไม่มีอาการ",
                    "text": "0"
                  },
                  "color": "#F9F7F7",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อยมาก",
                    "text": "1"
                  },
                  "color": "#F9F7F7",
                  "height": "sm",
                  "style": "secondary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "md",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อย",
                    "text": "2"
                  },
                  "color": "#DBE2EF",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ปานกลาง",
                    "text": "3"
                  },
                  "color": "#DBE2EF",
                  "height": "sm",
                  "style": "secondary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "md",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มาก",
                    "text": "4"
                  },
                  "color": "#3F72AF",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มากที่สุด",
                    "text": "5"
                  },
                  "color": "#112D4E",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "text",
              "text": "กรุณากรอกตามความเป็นจริงนะคะ",
              "margin": "lg",
              "size": "xs",
              "align": "end",
              "weight": "bold"
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "margin": "xl",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "margin": "xxl",
          "contents": [
            {
              "type": "text",
              "text": "ขอขอบพระคุณเป็นอย่างสูงที่ให้ความร่วมมือกับน้องหมอนะคะ",
              "margin": "xl",
              "align": "center",
              "weight": "bold",
              "color": "#FFFFFF",
              "wrap": True
            }
          ]
        }
      ]
    },
    "styles": {
      "header": {
        "backgroundColor": "#3F72AF"
      },
      "footer": {
        "backgroundColor": "#3F72AF"
      }
    }
  }
}

คำถามอาการน้ำมูกไหล = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "image",
          "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th.appspot.com/o/doctor%20(1).png?alt=media&token=74e146ed-e391-4cc6-95cf-6c58fc1032ca"
        },
        {
          "type": "text",
          "text": "Diagnos Question 4",
          "margin": "xl",
          "size": "lg",
          "align": "center",
          "weight": "bold",
          "color": "#FFFFFF"
        }
      ]
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "ข้อที่ 4",
              "size": "sm",
              "weight": "bold",
              "color": "#3F72AF"
            },
            {
              "type": "text",
              "text": "ท่านมีอาการน้ำมูกไหลหรือไม่คะ?",
              "size": "sm",
              "weight": "bold"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "xxl",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ไม่มีอาการ",
                    "text": "0"
                  },
                  "color": "#F9F7F7",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อยมาก",
                    "text": "1"
                  },
                  "color": "#F9F7F7",
                  "height": "sm",
                  "style": "secondary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "md",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อย",
                    "text": "2"
                  },
                  "color": "#DBE2EF",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ปานกลาง",
                    "text": "3"
                  },
                  "color": "#DBE2EF",
                  "height": "sm",
                  "style": "secondary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "md",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มาก",
                    "text": "4"
                  },
                  "color": "#3F72AF",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มากที่สุด",
                    "text": "5"
                  },
                  "color": "#112D4E",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "text",
              "text": "กรุณากรอกตามความเป็นจริงนะคะ",
              "margin": "lg",
              "size": "xs",
              "align": "end",
              "weight": "bold"
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "margin": "xl",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "margin": "xxl",
          "contents": [
            {
              "type": "text",
              "text": "ขอขอบพระคุณเป็นอย่างสูงที่ให้ความร่วมมือกับน้องหมอนะคะ",
              "margin": "xl",
              "align": "center",
              "weight": "bold",
              "color": "#FFFFFF",
              "wrap": True
            }
          ]
        }
      ]
    },
    "styles": {
      "header": {
        "backgroundColor": "#3F72AF"
      },
      "footer": {
        "backgroundColor": "#3F72AF"
      }
    }
  }
}

คำถามอาการเหนื่อยหอบ = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "image",
          "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th.appspot.com/o/doctor%20(1).png?alt=media&token=74e146ed-e391-4cc6-95cf-6c58fc1032ca"
        },
        {
          "type": "text",
          "text": "Diagnos Question 5",
          "margin": "xl",
          "size": "lg",
          "align": "center",
          "weight": "bold",
          "color": "#FFFFFF"
        }
      ]
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "ข้อที่ 5",
              "size": "sm",
              "weight": "bold",
              "color": "#3F72AF"
            },
            {
              "type": "text",
              "text": "ท่านมีอาการเหนื่อยหอบหรือไม่คะ?",
              "size": "sm",
              "weight": "bold"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "xxl",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ไม่มีอาการ",
                    "text": "0"
                  },
                  "color": "#F9F7F7",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อยมาก",
                    "text": "1"
                  },
                  "color": "#F9F7F7",
                  "height": "sm",
                  "style": "secondary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "md",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อย",
                    "text": "2"
                  },
                  "color": "#DBE2EF",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ปานกลาง",
                    "text": "3"
                  },
                  "color": "#DBE2EF",
                  "height": "sm",
                  "style": "secondary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "md",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มาก",
                    "text": "4"
                  },
                  "color": "#3F72AF",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มากที่สุด",
                    "text": "5"
                  },
                  "color": "#112D4E",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "text",
              "text": "กรุณากรอกตามความเป็นจริงนะคะ",
              "margin": "lg",
              "size": "xs",
              "align": "end",
              "weight": "bold"
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "margin": "xl",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "margin": "xxl",
          "contents": [
            {
              "type": "text",
              "text": "ขอขอบพระคุณเป็นอย่างสูงที่ให้ความร่วมมือกับน้องหมอนะคะ",
              "margin": "xl",
              "align": "center",
              "weight": "bold",
              "color": "#FFFFFF",
              "wrap": True
            }
          ]
        }
      ]
    },
    "styles": {
      "header": {
        "backgroundColor": "#3F72AF"
      },
      "footer": {
        "backgroundColor": "#3F72AF"
      }
    }
  }
}