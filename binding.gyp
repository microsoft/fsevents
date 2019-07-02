{
  "conditions": [
    ['OS=="mac"', {
      "targets": [{
        "target_name": "fsevents",
        "sources": ["fsevents.cc"],
        "xcode_settings": {
          "OTHER_LDFLAGS": [
            "-framework CoreFoundation -framework CoreServices"
          ]
        },
        "include_dirs": [
          "<!(node -e \"require('nan')\")"
        ]
      }, {
        "target_name": "action_after_build",
        "type": "none",
        "dependencies": ["fsevents"],
        "copies": [{
          "files": ["<(PRODUCT_DIR)/fsevents.node"],
          "destination": "./"
        }]
      }]
    }]
  ]
}
