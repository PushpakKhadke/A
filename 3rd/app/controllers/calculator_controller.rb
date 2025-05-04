class CalculatorController < ApplicationController
    def index
    end
  
    def add
      @result = params[:a].to_f + params[:b].to_f
      render plain: "Addition Result: #{@result}"
    end
  
    def subtract
      @result = params[:a].to_f - params[:b].to_f
      render plain: "Subtraction Result: #{@result}"
    end
  
    def multiply
      @result = params[:a].to_f * params[:b].to_f
      render plain: "Multiplication Result: #{@result}"
    end
  
    def divide
      b = params[:b].to_f
      @result = b == 0 ? "Cannot divide by zero" : params[:a].to_f / b
      render plain: "Division Result: #{@result}"
    end
  end
  