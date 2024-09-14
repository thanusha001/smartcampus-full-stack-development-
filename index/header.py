#!C:/Users/thanu/AppData/Local/Programs/Python/Python311/python.exe

def hdr():
	
	print("""
	<!doctype html>
	<html>
	<link rel="shortcut icon" href="Images/logo.png" />
	<head>
	<title>Smart Campus</title>
		<link href="Styles/StyleSheet.css" rel="Stylesheet" type="text/css" />
		<link href="Styles/Menu.css" rel="Stylesheet" type="text/css" />
		<link href="http://www.jqueryscript.net/css/jquerysctipttop.css" rel="stylesheet" type="text/css">
		<link rel="stylesheet" href="Slider/themes/default/default.css" type="text/css" media="screen" />
		<link rel="stylesheet" href="Slider/nivo-slider.css" type="text/css" media="screen" />
	</head>


	<body>
	   
		  <div>
		 <table border="0px solid black" width="100%">
		<tr><td width="220px" style="text-align:center;">
			<div class="container">
			<a class="navbar-brand" href="#">
			<img src="Images/logo.png" alt=""width="200px">
			</a></td>
			
			<td><!-- Slider Starts Here-->
				<script type="text/javascript" src="js/jssor.slider.min.js"></script>
				<!-- use jssor.slider.debug.js instead for debug -->
				<script>
					jssor_1_slider_init = function () {

						var jssor_1_SlideshowTransitions = [
					{ $Duration: 1200, $Opacity: 2 }
					];

						var jssor_1_options = {
							$AutoPlay: true,
							$SlideshowOptions: {
								$Class: $JssorSlideshowRunner$,
								$Transitions: jssor_1_SlideshowTransitions,
								$TransitionsOrder: 1
							},
							$ArrowNavigatorOptions: {
								$Class: $JssorArrowNavigator$
							},
							$BulletNavigatorOptions: {
								$Class: $JssorBulletNavigator$
							}
						};

						var jssor_1_slider = new $JssorSlider$("jssor_1", jssor_1_options);

						//responsive code begin
						//you can remove responsive code if you don't want the slider scales while window resizes
						function ScaleSlider() {
							var refSize = jssor_1_slider.$Elmt.parentNode.clientWidth;
							if (refSize) {
								refSize = Math.min(refSize, 1100);
								jssor_1_slider.$ScaleWidth(refSize);
							}
							else {
								window.setTimeout(ScaleSlider, 30);
							}
						}
						ScaleSlider();
						$Jssor$.$AddEvent(window, "load", ScaleSlider);
						$Jssor$.$AddEvent(window, "resize", $Jssor$.$WindowResizeFilter(window, ScaleSlider));
						$Jssor$.$AddEvent(window, "orientationchange", ScaleSlider);
						//responsive code end
					};
				</script>

				<style>
			
					.jssorb05 {
						position: absolute;
					}
					.jssorb05 div, .jssorb05 div:hover, .jssorb05 .av {
						position: absolute;
						/* size of bullet elment */
						width: 16px;
						height: 16px;
						background: url('Images/b05.png') no-repeat;
						overflow: hidden;
						cursor: pointer;
					}
					
					.jssorb05 div { background-position: -7px -7px; }
					.jssorb05 div:hover, .jssorb05 .av:hover { background-position: -37px -7px; }
					.jssorb05 .av { background-position: -67px -7px; }
					.jssorb05 .dn, .jssorb05 .dn:hover { background-position: -97px -7px; }

				
					.jssora12l, .jssora12r {
						display: block;
						position: absolute;
						/* size of arrow element */
						width: 30px;
						height: 46px;
						cursor: pointer;
						background: url('Images/a12.png') no-repeat;
						overflow: hidden;
					}
					.jssora12l { background-position: -16px -37px; }
					.jssora12r { background-position: -75px -37px; }
					.jssora12l:hover { background-position: -136px -37px; }
					.jssora12r:hover { background-position: -195px -37px; }
					.jssora12l.jssora12ldn { background-position: -256px -37px; }
					.jssora12r.jssora12rdn { background-position: -315px -37px; }
				</style>

				<div style="border:2px dashed #00737A; border-radius:15px; width: 820px;">
				<div id="jssor_1" style="position: relative; border-radius:15px; margin: 0 auto; top: 0px; left: 0px; width: 1100px; height: 225px; overflow: hidden; visibility: hidden;">
					<!-- Loading Screen -->
					<div data-u="loading" style="position: absolute; top: 0px; left: 0px;">
						<div style="filter: alpha(opacity=70); opacity: 0.7; position: absolute; display: block; top: 0px; left: 0px; width: 100%; height: 100%;"></div>
						<div style="position:absolute;display:block;background:url('Images/loading.gif') no-repeat center center;top:0px;left:0px;width:100%;height:100%;"></div>
					</div>
					<div data-u="slides" style="cursor: default; position: relative; top: 0px; left: 0px; width: 1100px; height: 300px; overflow: hidden;">
						<div data-p="112.50" style="display: none;">
							<img data-u="image" src="Slider/new1.jpg" />
						</div>
						<div data-p="112.50" style="display: none;">
							<img data-u="image" src="Slider/new2.jpeg" />
						</div>
						<div data-p="112.50" style="display: none;">
							<img data-u="image" src="Slider/new3.jpeg" />
						</div>
				
					</div>
					<!-- Bullet Navigator -->
					<div data-u="navigator" class="jssorb05" style="bottom:16px;right:6px;" data-autocenter="1">
						<!-- bullet navigator item prototype -->
						<div data-u="prototype" style="width:16px;height:16px;"></div>
					</div>
					
					<!-- Arrow Navigator -->
					<span data-u="arrowleft" class="jssora12l" style="top:123px;left:0px;width:30px;height:46px;" data-autocenter="2"></span>
					<span data-u="arrowright" class="jssora12r" style="top:123px;right:0px;width:30px;height:46px;" data-autocenter="2"></span>
						<a href="http://www.jssor.com" style="display:none">Jssor Slider</a>
				 </div>
				<script>
					jssor_1_slider_init();
				</script>
				</div>

				<!-- Slider Ends Here-->
			</td>
	   </tr>
		</table>
		</div>
		
		<!-- Content Place Holder Starts Here-->
		
		<div style="text-align:right;">
		
		</div>
		
		<!-- Content Place Holder Ends Here-->
	   
	</body>
	</html>

	""")
