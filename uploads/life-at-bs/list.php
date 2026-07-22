<?php
/*
 * Life at BS — Auto Gallery Scanner
 * 
 * Drop any images (.webp, .jpg, .jpeg, .png, .gif, .avif, .svg)
 * or videos (.mp4, .webm) into this folder and they will
 * automatically appear on the Life at BS page.
 *
 * No HTML editing required!
 */

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Cache-Control: public, max-age=60');

$dir = __DIR__;
$allowed_extensions = [
    // Images
    'webp', 'jpg', 'jpeg', 'png', 'gif', 'avif', 'svg',
    // Videos
    'mp4', 'webm'
];

$image_extensions = ['webp', 'jpg', 'jpeg', 'png', 'gif', 'avif', 'svg'];
$video_extensions = ['mp4', 'webm'];

$files = [];

if (is_dir($dir)) {
    $items = scandir($dir);
    foreach ($items as $item) {
        // Skip hidden files, directories, and this PHP file
        if ($item[0] === '.' || is_dir("$dir/$item") || $item === basename(__FILE__)) {
            continue;
        }
        
        $ext = strtolower(pathinfo($item, PATHINFO_EXTENSION));
        
        if (in_array($ext, $allowed_extensions)) {
            $filepath = "$dir/$item";
            $type = in_array($ext, $video_extensions) ? 'video' : 'image';
            
            $files[] = [
                'name' => $item,
                'type' => $type,
                'size' => filesize($filepath),
                'modified' => filemtime($filepath)
            ];
        }
    }
}

// Sort by modification date, newest first
usort($files, function($a, $b) {
    return $b['modified'] - $a['modified'];
});

echo json_encode($files);
?>
