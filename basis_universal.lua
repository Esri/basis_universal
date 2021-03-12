project "basis_universal"

dofile(_BUILD_DIR .. "/static_library.lua")

configuration { "*" }

uuid "E2587158-A6F8-4BF3-9A7D-9CB1C2F0A5FE"

defines {
  "BASISU_NO_ITERATOR_DEBUG_LEVEL",
}

includedirs {
  "transcoder",
}

files {
  "*.h",
  "*.c",
  "*.cpp",

  "transcoder/**.h",
  "transcoder/**.cpp",
}

excludes {
  "basisu_tool.cpp",
}

if (_PLATFORM_ANDROID) then
end

if (_PLATFORM_COCOA) then
end

if (_PLATFORM_IOS) then
end

if (_PLATFORM_LINUX) then
end

if (_PLATFORM_MACOS) then
end

if (_PLATFORM_WINDOWS) then
end

if (_PLATFORM_WINUWP) then
end
