<?php

namespace Drupal\Pages;

/**
 * Class AccessDenied
 * @package Drupal\Pages
 */
class AccessDenied extends NodePage
{
    /**
     * Declare UI map for this page here. CSS or XPath allowed.
     * public static $usernameField = '#username';
     * public static $formSubmitButton = "#mainForm input[type=submit]";
     */

    /**
     * @var string
     */
    public static $accessDeniedMessage = 'Sorry, access denied';
}
