# Copyright 2016 Google Inc.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
# GYP file to build performance testbench.
#
{
  'includes': [
    'apptype_console.gypi',
  ],
  'targets': [
    {
      'target_name': 'viewer',
      'type': 'executable',
      'includes' : [
        'gmslides.gypi',
      ],
      'include_dirs': [
        '../bench',
	'../experimental',
        '../gm',
        '../include/views',
        '../include/private',
	'../samplecode',
        '../src/core',
        '../src/effects',
        '../src/gpu',
        '../src/image',
        '../src/images',
        '../src/pathops',
        '../src/views/unix',
        '../tools/timer',
	'../tools',
      ],
      'sources': [
        '../gm/gm.cpp',

        '../src/views/unix/keysym2ucs.c',
        '<!@(python find.py ../tools/viewer "*.cpp")',

        # Samples
        '../samplecode/GMSampleView.h',
        '../samplecode/GMSampleView.cpp',
        '../samplecode/ClockFaceView.cpp',
        '../samplecode/OverView.cpp',
        '../samplecode/OverView.h',
        '../samplecode/PerlinPatch.cpp',
        '../samplecode/Sample2PtRadial.cpp',
        '../samplecode/SampleAAClip.cpp',
        '../samplecode/SampleAAGeometry.cpp',
        '../samplecode/SampleAARects.cpp',
        '../samplecode/SampleAARectModes.cpp',
        '../samplecode/SampleAll.cpp',
        '../samplecode/SampleAnimatedText.cpp',
        '../samplecode/SampleAnimBlur.cpp',
        '../samplecode/SampleApp.cpp',
        '../samplecode/SampleArc.cpp',
        '../samplecode/SampleAtlas.cpp',
        '../samplecode/SampleBigBlur.cpp',
        '../samplecode/SampleBigGradient.cpp',
        '../samplecode/SampleBitmapRect.cpp',
        '../samplecode/SampleBlur.cpp',
        '../samplecode/SampleCamera.cpp',
        '../samplecode/SampleChart.cpp',
        '../samplecode/SampleCircle.cpp',
        '../samplecode/SampleClip.cpp',
        '../samplecode/SampleClipDrawMatch.cpp',
        '../samplecode/SampleClock.cpp',
        '../samplecode/SampleCode.h',
        '../samplecode/SampleColorFilter.cpp',
        '../samplecode/SampleComplexClip.cpp',
        '../samplecode/SampleConcavePaths.cpp',
        '../samplecode/SampleDegenerateTwoPtRadials.cpp',
        '../samplecode/SampleDither.cpp',
        '../samplecode/SampleDitherBitmap.cpp',
        '../samplecode/SampleEffects.cpp',
        '../samplecode/SampleEmboss.cpp',
        '../samplecode/SampleFatBits.cpp',
        '../samplecode/SampleFillType.cpp',
        '../samplecode/SampleFilter.cpp',
        '../samplecode/SampleFilter2.cpp',
        '../samplecode/SampleFilterQuality.cpp',
        '../samplecode/SampleFilterFuzz.cpp',
        '../samplecode/SampleFontCache.cpp',
        '../samplecode/SampleFontScalerTest.cpp',
        '../samplecode/SampleFuzz.cpp',
        '../samplecode/SampleGradients.cpp',
        '../samplecode/SampleHairCurves.cpp',
        '../samplecode/SampleHairline.cpp',
        '../samplecode/SampleHairModes.cpp',
        '../samplecode/SampleHT.cpp',
        '../samplecode/SampleIdentityScale.cpp',
        '../samplecode/SampleLayerMask.cpp',
        '../samplecode/SampleLayers.cpp',
        '../samplecode/SampleLCD.cpp',
        '../samplecode/SampleLighting.cpp',
        '../samplecode/SampleLines.cpp',
        '../samplecode/SampleLitAtlas.cpp',
        '../samplecode/SampleLua.cpp',
        '../samplecode/SampleManyRects.cpp',
        '../samplecode/SampleMeasure.cpp',
        '../samplecode/SampleMegaStroke.cpp',
        '../samplecode/SamplePatch.cpp',
        '../samplecode/SamplePath.cpp',
        '../samplecode/SamplePathClip.cpp',
        '../samplecode/SamplePathFuzz.cpp',
        '../samplecode/SamplePathEffects.cpp',
        '../samplecode/SamplePictFile.cpp',
        '../samplecode/SamplePoints.cpp',
        '../samplecode/SamplePolyToPoly.cpp',
        '../samplecode/SampleQuadStroker.cpp',
        '../samplecode/SampleRectanizer.cpp',
        '../samplecode/SampleRegion.cpp',
        '../samplecode/SampleRepeatTile.cpp',
        '../samplecode/SampleShaders.cpp',
        '../samplecode/SampleShaderText.cpp',
        '../samplecode/SampleShip.cpp',
        '../samplecode/SampleSkLayer.cpp',
        '../samplecode/SampleSlides.cpp',
        '../samplecode/SampleStringArt.cpp',
        '../samplecode/SampleStrokePath.cpp',
        '../samplecode/SampleSubpixelTranslate.cpp',
        '../samplecode/SampleText.cpp',
        '../samplecode/SampleTextAlpha.cpp',
        '../samplecode/SampleTextBox.cpp',
        '../samplecode/SampleTextOnPath.cpp',
        '../samplecode/SampleTextureDomain.cpp',
        '../samplecode/SampleTiling.cpp',
        '../samplecode/SampleTinyBitmap.cpp',
        '../samplecode/SampleUnpremul.cpp',
        '../samplecode/SampleVertices.cpp',
        '../samplecode/SampleXfermodesBlur.cpp',
        '../samplecode/SampleXfer.cpp',
        '../src/views/SkTouchGesture.cpp',
	
        # PerlinNoise2
        '../experimental/SkPerlinNoiseShader2/SkPerlinNoiseShader2.cpp',
        '../experimental/SkPerlinNoiseShader2/SkPerlinNoiseShader2.h',

	# Lua
        '../src/utils/SkLuaCanvas.cpp',
        '../src/utils/SkLua.cpp',
      ],
      'sources!': [
        '../samplecode/SampleSkLayer.cpp', #relies on SkMatrix44 which doesn't compile
        '../samplecode/SampleFontCache.cpp', #relies on pthread.h
      ],      
      'dependencies': [
        'experimental.gyp:experimental',
        'flags.gyp:flags',
        'gputest.gyp:skgputest',
        'jsoncpp.gyp:jsoncpp',
	'lua.gyp:lua',
        'pdf.gyp:pdf',
        'skia_lib.gyp:skia_lib',
        'tools.gyp:crash_handler',
        'tools.gyp:proc_stats',
        'tools.gyp:resources',
        'tools.gyp:sk_tool_utils',
        'tools.gyp:timer',
        'tools.gyp:url_data_manager',
	'views.gyp:views',
	'xml.gyp:xml',
      ],
      'conditions' : [
        [ 'skia_os == "android"', {
          'dependencies': [
            'android_deps.gyp:Android_EntryPoint',
            'android_deps.gyp:native_app_glue',
          ],
          'link_settings': {
            'libraries': [
              '-landroid',
            ],
          },
        }],
        [ 'skia_os == "linux"', {
          'link_settings': {
            'libraries': [
              '-lX11-xcb',
            ],
          },
        }],
        ['skia_os != "android"', {
          'sources/': [ ['exclude', '_android.(h|cpp)$'],
          ],
        }],
        ['skia_os != "linux"', {
          'sources/': [ 
            ['exclude', '_unix.(h|cpp)$'],
            ['exclude', 'keysym2ucs.c'],
          ],
        }],
        ['skia_os != "win"', {
          'sources/': [ ['exclude', '_win.(h|cpp)$'],
          ],
        }],
      ],
    },
  ],
}
