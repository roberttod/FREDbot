FILE(REMOVE_RECURSE
  "../msg_gen"
  "../src/speech_synth/msg"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/speech_synth/msg/__init__.py"
  "../src/speech_synth/msg/_emote_text.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
