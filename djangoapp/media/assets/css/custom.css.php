<?php 
header("Content-type: text/css; charset=utf-8");
$absolute_path = __FILE__;
$path_to_file = explode( 'wp-content', $absolute_path );
$path_to_wp = $path_to_file[0];
require_once( $path_to_wp . '/wp-load.php' );
global $wtn_theme;
?>

.headerimage {
	background-image: url(<?php echo $wtn_theme['defaultimgheader']['url'];?>);
}

.headerimage.homeimg {
	background-image: url(<?php echo $wtn_theme['homeimg']['url'];?>);
}

<?php if($wtn_theme['checkifaccentcolor'] == '1') { ?>
a, a:hover, .color, .colorme, .wowitemboxinner .edd-submit.button:hover, .pagination a.inactive:hover, #sidemenu li a:hover, #sidemenu li a.open, .post-content .wowmetaposts span a:hover, ul.edd-taxonomy-widget li a:hover, .edd_downloads_list #edd_download_pagination .page-numbers.current, .edd_downloads_list #edd_download_pagination .page-numbers:hover, .navbar-default .navbar-nav>.active>a,.navbar-default .navbar-nav>.active>a:hover,.navbar-default .navbar-nav>.active>a:focus, .dropdown-menu>li>a:focus,.dropdown-menu>li>a:hover,.dropdown-menu>.active>a,.dropdown-menu>.active>a:focus,.dropdown-menu>.active>a:hover {
	color:<?php echo $wtn_theme['accent-color']; ?>;
}

input[type=submit]:hover, #edd_checkout_form_wrap input[type="submit"].edd-submit, .pagination .current, .wowsortitems:before, .templatemyaccount .shoppingcartarea .edd_checkout a:hover, .contentdownloadphp .edd-add-to-cart.button.edd-submit, .contentdownloadphp .edd_go_to_checkout.button.edd-submit, .notfoundbadge:hover, .excerpttext .readmore, .widget_edd_product_details .edd_purchase_submit_wrapper a.edd-add-to-cart.edd-has-js,.widget_edd_product_details .edd_purchase_submit_wrapper a.edd-add-to-cart.edd-no-js, .widget_edd_product_details .edd-add-to-cart.edd-submit, footer .widget_wysija_cont .wysija-submit, .actionbeforefooter, .navbar-default .navbar-toggle:hover,.navbar-default .navbar-toggle:focus 	{
	background-color:<?php echo $wtn_theme['accent-color']; ?>;
}

.navbar-nav>li>.dropdown-menu, .navbar-nav li.menu-item-has-children ul.sub-menu {
	border-top: 3px solid <?php echo $wtn_theme['accent-color']; ?>;
}

li.checkoutmenu, .edd_downloads_list #edd_download_pagination .page-numbers.current, .edd_downloads_list #edd_download_pagination .page-numbers:hover {
	border: <?php echo $wtn_theme['accent-color']; ?> 1px solid;
}

footer.themefooter h3.widget-title:after {
	border-top-color:<?php echo $wtn_theme['accent-color']; ?>;
}

.edd_download_inner input[type="radio"]:checked {
	border: 6px solid <?php echo $wtn_theme['accent-color']; ?>;
}
<?php } ?>	

<?php if( $wtn_theme['homepage_itemsperpage'] == '3' ) {?>
	#homepagetemplate .wowitembox {width:33.33%;}
<?php } ?>

<?php if($wtn_theme['shop_menucart'] == '0') { ?>
	li.checkoutmenu {display:none;}
	@media only screen and (min-width: 768px){
	.navbar-right {margin-right: -15px;}
	}
<?php } ?>

<?php if($wtn_theme['shop_showsortableselect'] == '0') { ?>
	.sortitemsarea {display:none;}
<?php } ?>

<?php if($wtn_theme['shop_showpageresults'] == '0') { ?>
	.pagesit {display:none;}
<?php } ?>

<?php if($wtn_theme['shop_showsku'] == '0') { ?>
	.entrysku {display:none;}
<?php } ?>

<?php if($wtn_theme['checkifboxedlayout'] == '1') { ?>
	body, #wow-menu.navbar-default {width: 90%;	margin: 0px auto;}
	body {
		background-color:<?php echo $wtn_theme['bodyboxedlayout']['background-color'];?>; 
		background-image:url(<?php echo $wtn_theme['bodyboxedlayout']['background-image'];?>);
		background-repeat:<?php echo $wtn_theme['bodyboxedlayout']['background-repeat'];?>;
		background-position:<?php echo $wtn_theme['bodyboxedlayout']['background-position'];?>;
		background-size:<?php echo $wtn_theme['bodyboxedlayout']['background-size'];?>;
		background-attachment:<?php echo $wtn_theme['bodyboxedlayout']['background-attachment'];?>;
	}
   .boxedlayout {background-color:#fff;}
<?php } ?>

<?php echo $wtn_theme['custom-css']; ?>