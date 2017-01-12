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
    helm
    jedi
    projectile
    helm-projectile
    helm-ag))

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

;; enable python IDE
(elpy-enable)
(add-hook 'python-mode-hook 'jedi:setup)
(setq jedi:complete-on-dot t) 
(setq jedi:use-shortcuts t)

;;ad-hoc functions
(defun my-put-file-name-on-clipboard ()
  "Put the current file name on the clipboard"
  (interactive)
  (let ((filename (if (equal major-mode 'dired-mode)
                      default-directory
                    (buffer-file-name))))
    (when filename
      (with-temp-buffer
        (insert filename)
        (clipboard-kill-region (point-min) (point-max)))
      (message filename))))

(defun my-delete-this-buffer-and-file ()
  "Removes file connected to current buffer and kills buffer."
  (interactive)
  (let ((filename (buffer-file-name))
        (buffer (current-buffer))
        (name (buffer-name)))
    (if (not (and filename (file-exists-p filename)))
        (error "Buffer '%s' is not visiting a file!" name)
      (when (yes-or-no-p "Are you sure you want to remove this file? ")
        (delete-file filename)
        (kill-buffer buffer)
        (message "File '%s' successfully removed" filename)))))

;;behaviours
(global-auto-revert-mode t)

;;key bindings
(global-set-key (kbd "M-x") 'helm-M-x)
(global-unset-key "\C-z") ;;C-z as a gateway for my shortcuts
(global-set-key (kbd "C-z C-S-f") 'helm-projectile-ag)
(global-set-key (kbd "C-z C-S-n") 'helm-projectile)
(global-set-key (kbd "C-z C-S-M-c") 'my-put-file-name-on-clipboard)
(global-set-key (kbd "C-z C-M-k") 'my-delete-this-buffer-and-file)

;;folders setup
(getenv "HOME")
(setq default-directory "~/projects/")
(setq tags-table-list
      '("~/projects/"))

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages
   (quote
    (material-theme better-defaults multiple-cursors helm elpy)))
 '(reb-re-syntax (quote string)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
