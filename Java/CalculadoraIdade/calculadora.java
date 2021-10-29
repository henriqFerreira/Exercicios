package CalculadoraIdade;
import java.util.Scanner;

public class calculadora {
    // Em java, 'main' é o programa principal
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int anoNasc;
        System.out.println("Entre com o ano de nascimento: ");
        anoNasc = teclado.nextInt();
        calculaIdadeAproximada(anoNasc);
        teclado.close();
    }

    public static void calculaIdadeAproximada(int anoNasc) {
        int idade = 2021 - anoNasc;
        System.out.println("Idade aproximada: " + idade);
    }
}
