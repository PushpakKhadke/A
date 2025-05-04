Rails.application.routes.draw do
  root 'application#calculator'
  post 'calculate', to: 'application#calculate'
end
