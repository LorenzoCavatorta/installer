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
  '(multiple-cursors
    better-defaults
    material-theme
    helm
    jedi
    projectile
    helm-projectile
    helm-ag
    dumb-jump
    ;;column-marker
    csv-mode))

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
(setq-default frame-title-format "%b (%f)") ;;shows file path for current buffer in the frame title
;;(add-hook 'python-mode-hook (lambda () (interactive) (column-marker-1 80)))

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

(defun uniquify-all-lines-region (start end)
  "Find duplicate lines in region START to END keeping first occurrence."
  (interactive "*r")
  (save-excursion
    (let ((end (copy-marker end)))
      (while
          (progn
            (goto-char start)
            (re-search-forward "^\\(.*\\)\n\\(\\(.*\n\\)*\\)\\1\n" end t))
        (replace-match "\\1\n\\2")))))

(defun uniquify-all-lines-buffer ()
  "Delete duplicate lines in buffer and keep first occurrence."
  (interactive "*")
  (uniquify-all-lines-region (point-min) (point-max)))

;;behaviours
(global-auto-revert-mode t)
;;(dumb-jump-mode) ;; would activate dumb jump mode key bindings

;;key bindings
(global-set-key (kbd "M-x") 'helm-M-x)
(global-unset-key "\C-z") ;;C-z as a gateway for my shortcuts
(global-set-key (kbd "C-z C-S-f") 'helm-projectile-ag)
(global-set-key (kbd "C-z C-S-n") 'helm-projectile)
(global-set-key (kbd "C-z C-S-M-c") 'my-put-file-name-on-clipboard)
(global-set-key (kbd "C-z C-M-k") 'my-delete-this-buffer-and-file)
(global-set-key (kbd "C-z C-b") 'dumb-jump-go)
(global-set-key (kbd "C-z C-z C-b") 'dumb-jump-go-other-window)
(global-set-key (kbd "C-z C-q") 'dumb-jump-quick-look)
(global-set-key (kbd "C-z C-p") 'dumb-jump-back)
;;windows bindings
(global-set-key (kbd "s-M-<left>") 'shrink-window-horizontally)
(global-set-key (kbd "s-M-<right>") 'enlarge-window-horizontally)
(global-set-key (kbd "s-M-<down>") 'shrink-window)
(global-set-key (kbd "s-M-<up>") 'enlarge-window)
(global-set-key (kbd "s-<left>") 'windmove-left)          ; move to left window
(global-set-key (kbd "s-<right>") 'windmove-right)        ; move to right window
(global-set-key (kbd "s-<up>") 'windmove-up)              ; move to upper window
(global-set-key (kbd "s-<down>") 'windmove-down)          ; move to lower window
(global-set-key (kbd "C-x m") 'set-rectangular-region-anchor)


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
