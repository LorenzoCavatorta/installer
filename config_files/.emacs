;; INSTALL PACKAGES
;; --------------------------------------

;;repos
(require 'package)

(add-to-list 'package-archives
       '("melpa" . "http://melpa.org/packages/") t)

(add-to-list 'package-archives '
	     ("marmalade" . "http://marmalade-repo.org/packages/") t)

(package-initialize)
(when (not package-archive-contents)
  (package-refresh-contents))

;;chosen packages
(defvar myPackages
  '(better-defaults
    material-theme
    helm))

(mapc #'(lambda (package)
    (unless (package-installed-p package)
      (package-install package)))
      myPackages)

;; appearance
(menu-bar-mode -1)
(toggle-scroll-bar -1)
(tool-bar-mode -1)
(setq inhibit-startup-message t) ;; hide the startup message
(load-theme 'material t)  ;; load material theme
(global-linum-mode t) ;; enable line numbers globally
(add-to-list 'default-frame-alist '(fullscreen . maximized))

(elpy-enable)

;;key bindings
(global-set-key (kbd "M-x") 'helm-M-x)

(getenv "HOME")
(setq default-directory "~/projects/")
